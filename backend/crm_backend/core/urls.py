from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.views import GoogleCalendarAPIView, dashboard_statistics

router = DefaultRouter()


urlpatterns = [
    path('google/calendar/auth/',GoogleCalendarAPIView.as_view(),name='google-calendar-auth'),
    path('dashboard-statistics',dashboard_statistics,name='dashboard-statistics')
]