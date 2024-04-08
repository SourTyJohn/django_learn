from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogMessage
        fields = ('text', )
        widgets = {
            'text': forms.Textarea()
        }

