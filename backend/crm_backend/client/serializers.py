from rest_framework import serializers
from .models import Client , Note
from team.serializers import UserSerializer


class NoteSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Note
        fields = (
            'id',
            'name',
            'body',
            'created_by',
            'created_at'
        )
        read_only_files = ('modified_at')



class ClientSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    class Meta:
        model = Client
        fields = (
            'id',
            'name',
            'contact_person',
            'email',
            'phone',
            'website',
            'created_by',
            'created_at',
            'modified_at',
            'profile_picture',
            'status',
            'client_address',
            'assigned_to',
            'source',
            'last_contacted_date',
            'address'
        )
        read_only_fields = ('created_by',
                            'created_at',
                            'modified_at',
                            'team')


