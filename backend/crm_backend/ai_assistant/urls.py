from django.urls import path

from ai_assistant.views import assistant

urlpatterns = [
    path('assistant/',assistant,name='assistant'),
]