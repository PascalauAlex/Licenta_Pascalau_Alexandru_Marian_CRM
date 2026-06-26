from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from userprofile.models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    #Check if the User has attached 'userprofile'
    #Using userprofile defined in userprofile.models.UserProfile
    if hasattr(instance,'userprofile'):
        instance.userprofile.save()

@receiver(post_save, sender=User, dispatch_uid="send_welcome_email")
def send_welcome_email(sender, instance, created, **kwargs):
    """Send a welcome email when a new user is created"""
    print(f"Sending mail to: {instance.username}")
    
    if created:
        print('Trimit mailul acum...')
        send_mail(
            'Welcome!',
            f"Thanks for signing in: {instance.username}",
            "pascalaualex63@gmail.com",
            [instance.email],
            fail_silently=True,
        )
        print('Email trimis...')



