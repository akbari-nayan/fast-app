from django.db import models
from django.core.validators import FileExtensionValidator
from service_pr.models import Client,ServiceProvider
# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=30,blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/',default='avatar.png' ,validators=[FileExtensionValidator(['png','jpg','jpeg'])],blank=True)
    subscribed  = models.ManyToManyField(Client,  blank=True, related_name='subscribes')   
    updated = models.DateTimeField( auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE, related_name='posts' ) 


    def __str__(self):
        return str(self.service_name)

    class Meta:
        ordering = ('-created',)
    





SUBSCRIPTION_TYPES = (
        ('Subscribe', 'Subscribe'),
        ('Unsubscribe', 'Unnsubscribe'),
    )



class Subscription(models.Model):
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=SUBSCRIPTION_TYPES, max_length=11)
    updated = models.DateTimeField( auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
    