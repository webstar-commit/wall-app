from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save



def send_welcome_email(sender, instance,created, **kwargs):
    if created:
        send_mail(
            settings.WELCOME_EMAIL_TITLE,
            settings.WELCOME_EMAIL_BODY,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=True,
        )



post_save.connect(send_welcome_email, sender=User)