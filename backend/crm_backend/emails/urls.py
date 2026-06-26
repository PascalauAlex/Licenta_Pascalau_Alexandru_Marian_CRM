from django.urls import include , path
from rest_framework.routers import DefaultRouter
from .views import SendEmailView, LeadEmailListView

from emails.views import SendEmailView


urlpatterns = [
    path('send-mail/',SendEmailView.as_view(),name='send-mail'),
    path('email-lead/<int:lead_id>/',LeadEmailListView.as_view() , name='email-lead'),
    path('email-client/<int:client_id>/',LeadEmailListView.as_view(),name='email-client')
]