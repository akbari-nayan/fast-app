from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    
    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username contain alphanumeric charactor')

        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
        