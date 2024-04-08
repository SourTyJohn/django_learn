from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('reg_page', views.register, name='register'),
    path('blog', views.add_blog, name='blog')
]
