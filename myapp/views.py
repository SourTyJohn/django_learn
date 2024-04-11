from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from django.http import HttpRequest
from . import forms
from . import models


def index(request: HttpRequest):
    return render(request, "index.html")


def register(request: HttpRequest):

    # -- GET --
    if request.method == 'GET':
        reg_form = forms.UserFormRegister()
        context = {'form': reg_form}
        return render(request, 'register_page.html', context)

    # -- POST --
    reg_form = forms.UserFormRegister(request.POST)
    queryset = models.User.objects.all()

    if reg_form.is_valid():
        reg_form.save()
        return redirect( index )

    return redirect( register )


def add_blog(request: HttpRequest):
    # -- GET --
    if request.method == 'GET':
        blog_form = forms.BlogForm()
        context = {'form': blog_form}
        return render(request, 'add_blog.html', context)

    # -- POST --
    blog_form = forms.BlogForm(request.POST, sender=None)
    if blog_form.is_valid():
        blog_form.save()
        return redirect( index )

    return redirect( add_blog )


@require_GET
def blogs(request: HttpRequest):
    context = {}
    return render(request, 'blogs_page.html', context)
