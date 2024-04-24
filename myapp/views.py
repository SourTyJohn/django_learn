from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpRequest
from . import forms
from . import models


def index(request: HttpRequest):
    return redirect("/blogs_page/1/")


def blogs(request: HttpRequest, page_num):
    template_kwargs = { 'messages': models.BlogMessage.get_page( int(page_num) ) }
    return render(request, "blogs_page.html", template_kwargs)


def register(request: HttpRequest):

    # -- GET --
    if request.method == 'GET':
        template_kwargs = { 'form': forms.UserFormRegister() }
        return render(request, 'register_page.html', template_kwargs)

    # -- POST --
    reg_form = forms.UserFormRegister(request.POST)

    if not reg_form.is_valid():
        return redirect( register )

    username = reg_form.cleaned_data.get('username')
    if models.User.objects.filter(username=username).exists():
        messages.info(request, 'Имя пользователя занято')
        return redirect( register )

    user = reg_form.save()
    user.set_password( reg_form.cleaned_data.get('password') )
    user.save()

    return redirect( login_p )


def login_p(request: HttpRequest):

    # -- GET --
    if request.method == 'GET':
        template_kwargs = { 'form': forms.UserFormLogin() }
        return render(request, 'login_page.html', template_kwargs)

    # -- POST --
    login_form = forms.UserFormLogin(request.POST)

    if not login_form.is_valid():
        return redirect( login_p, errors=login_form.errors )

    password = login_form.cleaned_data.get('password')
    username = login_form.cleaned_data.get('username')

    if not models.User.objects.filter(username=username).exists():
        messages.info(request, 'Неверное имя пользователя!')
        return redirect( login_p )

    user = authenticate(request, password=password, username=username)

    if user is None:
        messages.info(request, 'Неверный пароль!')
        return redirect( login_p )

    login(request, user)
    return redirect(blogs)


def add_blog(request: HttpRequest):
    # -- GET --
    if request.method == 'GET':
        blog_form = forms.BlogForm()
        from_kwargs = {'form': blog_form, 'user': request.user}
        return render(request, 'add_blog.html', from_kwargs)

    # -- POST --
    if request.user is None:
        return redirect( add_blog )

    blog_form = forms.BlogForm(request.POST, sender=request.user)
    if blog_form.is_valid():
        blog_form.save()
        return redirect(blogs)

    return redirect( add_blog )


@require_GET
def show_message(request: HttpRequest, message_id):
    if request.user is None:
        return redirect( register )

    template_args = { 'message': models.BlogMessage.get_by_id(message_id) }
    return render(request, "blog_show.html", template_args)


