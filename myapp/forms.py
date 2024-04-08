from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }


class NewBlogForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
