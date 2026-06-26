import django_filters
from lead.models import Lead

class LeadFilter(django_filters.FilterSet):
    class Meta:
        model = Lead
        fields = {
            'company' : ['iexact','icontains'],
            'status' : ['exact'],
            'priority' : ['exact'],
            'assigned_to':['exact']
        }
