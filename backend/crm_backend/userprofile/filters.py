import django_filters
from django.contrib.auth.models import User


class UserFilter(django_filters.FilterSet):
    class Meta:
        fields = {
            'last_name':['iexact'],
            'first_name':['iexact']
        }
