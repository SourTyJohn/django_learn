from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


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

    @classmethod
    def get_all_posts(cls):
        return list(cls.objects.all())
