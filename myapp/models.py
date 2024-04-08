from django.db import models


class User(models.Model):
    user_name = models.CharField(
        verbose_name='Имя пользователя', max_length=64
    )
    email = models.EmailField(
        verbose_name='Почта', max_length=32
    )
    password = models.CharField(
        verbose_name='Пароль', max_length=64
    )

    def __str__(self):
        return f'<USER {self.email}>'
