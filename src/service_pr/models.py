from django.db import models
from users.models import CustomUser

# Create your models here.
class ServiceProvider(models.Model):
    service_provider_id = models.AutoField(primary_key=True)
    name = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.name)
    

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    


