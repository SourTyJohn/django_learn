from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('reg_page', views.reg_page, name='register'),
    path('blog', views.blog_page, name='blog')
]
