from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser




class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None