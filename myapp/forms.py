from django import forms


class RegisterForm(forms.Form):
    user_name = forms.CharField(label='Имя пользователя', max_length=64)
    password = forms.CharField(label='Пароль', max_length=64)


class NewBlogForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
