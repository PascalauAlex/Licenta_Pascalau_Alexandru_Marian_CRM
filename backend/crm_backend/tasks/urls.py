from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet , LeadTaskViewSet

router = DefaultRouter()
router.register('tasks',TaskViewSet, basename='tasks')


urlpatterns = [
    path('',include(router.urls)),
    path('lead-tasks/<int:pk>/', view=LeadTaskViewSet.as_view({
        'get': 'list',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    })),
]