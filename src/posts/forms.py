from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    author = forms.CharField(widget = forms.HiddenInput(), required = False)
    class Meta:
        model = Post
        fields = ('service_name','content','image')


class PostIdForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ('post_id',)