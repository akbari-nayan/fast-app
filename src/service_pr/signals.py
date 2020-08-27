from django.db.models.signals import post_save
from users.models import CustomUser
from django.dispatch import receiver
from .models import ServiceProvider,Client


# init.py
# apps.py
@receiver(post_save, sender=CustomUser)
def post_save_create_client_or_service_provider(sender,instance, **kwargs):
    print(sender,instance.is_client)
    if instance.is_client:
        Client.objects.get_or_create(name=instance)
    elif instance.is_service_provider:
        ServiceProvider.objects.get_or_create(name=instance)


