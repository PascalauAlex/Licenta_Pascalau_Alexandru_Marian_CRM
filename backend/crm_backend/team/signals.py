import threading
from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver
from team.models import Team



@receiver(post_save,sender=Team)
def auto_delete_invite_code(sender,instance,**kwargs):
    print("=== Auto delete invite fired ===")
    #Checks only for updates with invite code
    if instance.invite_code is None:
        return

    def clear_invite_code():
        Team.objects.filter(pk=instance.pk).update(invite_code=None)
        print(f"=== Invite code for {instance.name} ended ===")

    print("=== Invite code expires in 60 seconds ===")
    timer = threading.Timer(60,clear_invite_code)
    timer.daemon = True # do not block the server shutdown
    timer.start()


