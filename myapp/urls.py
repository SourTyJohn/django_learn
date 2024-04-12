from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.register, name='register'),
    path('login', views.login_p, name='login'),
    path('blog', views.add_blog, name='blog')
]
