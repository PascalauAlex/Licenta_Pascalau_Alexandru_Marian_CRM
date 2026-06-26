import django_filters
from tasks.models import Tasks

class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = Tasks
        fields = {
            'status': ['exact'],
            'assigned_to':['exact']
        }