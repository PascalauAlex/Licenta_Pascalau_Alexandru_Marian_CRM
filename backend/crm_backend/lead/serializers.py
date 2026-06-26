import decimal

from django.db import transaction
from key_value.aio.wrappers import retry

from rest_framework import serializers
from products.models import LeadProductInterest

from core.models import Address
from .models import Lead, LeadNote, LostReason
from team.serializers import UserSerializer
from core.serializer import AdressSerializer
from products.serializer import LeadProductInterestSerializer
from team.models import User



class LostReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostReason
        fields = (
            'id',
            'name',
            'slug',
            'category',
            'description',
        )
        read_only_fields = ('created_at','created_by')


class LeadSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    address = AdressSerializer(required=False)
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='assigned_to',
        write_only=True,
        required=True
    )
    product_interests = LeadProductInterestSerializer(many=True, required=False)
    lost_reason_id = serializers.PrimaryKeyRelatedField(
        queryset=LostReason.objects.all(),
        source = 'lost_reason',
        write_only=True,
        required=False,
        allow_null=True
    )
    lost_reason = LostReasonSerializer(read_only=True)
    class Meta:
        model = Lead
        fields = (
            'id',
            'company',
            'contact_person',
            'email',
            'phone',
            'website',
            'confidence',
            'status',
            'priority',
            'created_by',
            'estimated_value',
            'assigned_to',
            'created_at',
            'modified_at',
            'checklist',
            'address',
            'lost_reason',
            'source',
            'next_follow_up_date',
            'last_contacted_date',
            'expected_close_date',
            'lost_reason_details',
            'lost_at',
            'product_interests',
            'assigned_to_id',
            'lost_reason_id'
        )
        read_only_fields = ('created_by', 'created_at', 'modified_at','priority','confidence','estimated_value')



    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        interest_data = validated_data.pop('product_interests', [])


        with transaction.atomic():
            if address_data:
                validated_data['address'] = Address.objects.create(**address_data)

            lead = Lead.objects.create(**validated_data)


            interests = []
            for item in interest_data:
                if item.get('estimated_value') is None:
                    item['estimated_value'] = item['product'].base_price * item['quantity']
                    item['estimated_value'] = item['estimated_value'] - item['estimated_value'] * decimal.Decimal(item['discount'] / 100)
                interests.append(LeadProductInterest(lead=lead, **item))
            LeadProductInterest.objects.bulk_create(interests)
            lead.recompute_estimated_value()

        return lead

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        interest_data = validated_data.pop('product_interests', None)

        with transaction.atomic():

            if address_data is not None:
                if instance.address:
                    for attr, value in address_data.items():
                        setattr(instance.address, attr, value)
                    instance.address.save()
                else:
                    instance.address = Address.objects.create(**address_data)


            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.save()


            if interest_data is not None:
                instance.product_interests.all()
                interests = []
                for item in interest_data:
                    if item.get('estimated_value') is None:
                        item['estimated_value'] = item['product'].base_price * item['quantity']
                        item['estimated_value'] = item['estimated_value'] - item['estimated_value'] * decimal.Decimal(item['discount'] / 100)
                    interests.append(LeadProductInterest(lead=instance, **item))
                LeadProductInterest.objects.bulk_create(interests)
                instance.recompute_estimated_value()

        return instance







class LeadNoteSerializer(serializers.ModelSerializer):
    created_by_name = serializers.ReadOnlyField(source='created_by.first_name')
    class Meta:
        model = LeadNote
        fields = (
            'id',
            'name',
            'body',
            'created_by_name',
            'created_at',
            'modified_at',
        )
        read_only_fields = ('created_by', 'created_at', 'modified_at')


























