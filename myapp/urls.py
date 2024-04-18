from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.register, name='register'),
    path('login/', views.login_p, name='login'),
    path('blog/', views.add_blog, name='blog'),

    path('logout/', LogoutView.as_view(), name="logout"),

    path('show_message/<slug:message_id>', views.msg_action, name='show_message')
]
