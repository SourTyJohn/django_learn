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


class BlogMessage(models.Model):
    # hidden
    sender = models.ForeignKey('User', on_delete=models.PROTECT)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

    # form
    text = models.CharField(
        verbose_name='Содержание', max_length=128
    )

    def __str__(self):
        return f'<BLOG {self.sender}>'
