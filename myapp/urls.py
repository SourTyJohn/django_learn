from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blogs_page/<slug:page_num>/', views.blogs, name='blogs_page'),

    path('blog/', views.add_blog, name='blog'),

    path('show_message/<slug:message_id>/', views.show_message, name='show_message'),

    path('login/', views.login_p, name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registration/', views.register, name='register'),
]
