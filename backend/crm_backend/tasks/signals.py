from django.db.models.signals import post_save
from django.dispatch import receiver


from .models import Tasks
from core.calendar_service import create_event_for_task


@receiver(post_save, sender=Tasks)
def push_task_to_calendar(sender, instance, created, **kwargs):
    if created:
        try:
            create_event_for_task(instance)
        except Exception as e:
            print('CALENDAR ERROR',e)



            