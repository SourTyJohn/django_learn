from django.shortcuts import render, redirect
from django.http import HttpRequest
from . import forms


def index(request: HttpRequest):
    return render(request, "index.html")


def reg_page(request: HttpRequest):

    # -- GET --
    if request.method == 'GET':
        reg_form = forms.UserForm()
        return render(request, 'register_page.html', {'form': reg_form})

    # -- POST --
    reg_form = forms.UserForm(request.POST)
    if reg_form.is_valid():
        reg_form.save()
        return redirect( index )

    return redirect( reg_page )


def blog_page(request: HttpRequest):
    # -- GET --
    if request.method == 'GET':
        blog_form = forms.NewBlogForm
        return render(request, 'blog_page.html', {'form': blog_form})

    # -- POST --
