from django import forms
from . import models


class UserFormRegister(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
        labels = {
            'username': 'Имя Пользователя',
            'email': 'Электронная Почта',
            'password': 'Пароль'
        }


class UserFormLogin(forms.Form):
    username = forms.CharField(
        max_length=models.User._meta.get_field('username').max_length,
        label=UserFormRegister.Meta.labels['username']
    )
    password = forms.CharField(
        max_length=models.User._meta.get_field('password').max_length,
        label=UserFormRegister.Meta.labels['password'],
        widget=forms.PasswordInput
    )


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogMessage
        fields = ('title', 'text', )
        widgets = {
            'text': forms.Textarea()
        }
        labels = {
            'title': 'Заголовок',
            'text': 'None'
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
