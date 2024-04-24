from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AbstractUser
from .settings import MESSAGES_PER_PAGE


class User(AbstractUser):
    pass


class BlogMessage(models.Model):
    objects = models.Manager()

    # hidden
    sender = models.ForeignKey('User', on_delete=models.PROTECT)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

    # form
    title = models.CharField(
        verbose_name='Заголовок', max_length=128
    )
    text = models.CharField(max_length=2048)

    def __str__(self):
        return f'<BLOG {self.sender}>'

    @classmethod
    def get_page(cls, page, per_page=MESSAGES_PER_PAGE, order_by='id'):
        return list(
            cls.objects.order_by(order_by)[ (page - 1) * per_page:page * per_page ]
        )

    @classmethod
    def get_by_id(cls, _id):
        return get_object_or_404(cls, pk=_id)


class LikeDislike(models.Model):
    objects = models.Manager()

    # hidden
    user = models.ForeignKey("User", on_delete=models.PROTECT)
    message = models.ForeignKey("BlogMessage", on_delete=models.PROTECT)
    is_like = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_message_likes_dislikes(cls, message: "BlogMessage"):
        query = cls.objects.filter(message=message)
        likes = len(query.filter(is_like=True).all())
        dislikes = len(query.filter(is_like=False).all())
        return likes, dislikes
