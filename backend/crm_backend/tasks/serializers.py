from django.contrib.auth.models import User
from rest_framework import serializers

from team.serializers import UserSerializer
from .models import Tasks , TaskAutomationRule
from lead.serializers import LeadSerializer
from lead.models import Lead



class TaskSerializers(serializers.ModelSerializer):
    lead = LeadSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    lead_id = serializers.PrimaryKeyRelatedField(
        queryset=Lead.objects.all(), source='lead', write_only=True, required=False
    )
    assigned_to_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='assigned_to',
        write_only=True,
        required=False
    )
    class Meta:
        model = Tasks
        fields = (
            'id',
            'title',
            'description',
            'status',
            'due_date',
            'lead',
            'lead_id',
            'assigned_to',
            'finished_date',
            'assigned_to_id'
        )

class TaskAutomationRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAutomationRule
        fields = '__all__'