from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LeadViewSet, LeadNoteViewSet, LostReasonViewSet

router = DefaultRouter()
router.register('leads', LeadViewSet, basename='leads')
router.register('lead-notes',LeadNoteViewSet, basename='leadNotes')
router.register('lost-reason',LostReasonViewSet, basename='lostReason')

urlpatterns = [
    path('',include(router.urls)),
]