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

    def __init__(self, *args, **kwargs):
        attrs = {
            'sender': kwargs.pop('sender', None),
            'likes': kwargs.pop('likes', 0),
            'dislikes': kwargs.pop('dislikes', 0)
        }
        super().__init__(*args, **kwargs)
        for key, value in attrs.items():
            setattr(self.instance, key, value)
