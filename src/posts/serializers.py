from rest_framework import serializers
from .models import Post
from users.models import CustomUser
from service_pr.models import ServiceProvider,Client

class CustomUserSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ('id','username','email')

class ServiceProviderSerilizer(serializers.ModelSerializer):
    name = CustomUserSerilizer()
    class Meta:
        model = ServiceProvider
        fields = ('service_provider_id','name')


class ClientSerilizer(serializers.ModelSerializer):
    name = CustomUserSerilizer()
    class Meta:
        model = Client
        fields = ('client_id','name')



class PostSerializer(serializers.ModelSerializer):
    author = ServiceProviderSerilizer()
    # subscribed = ClientSerilizer()
    class Meta:
        model = Post
        fields = ('__all__' )
        depth = 1

