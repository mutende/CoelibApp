from services.forms import Short_CourseForm, Music_ProductionForm, CommentForm,Studio_SessionForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime

def home(request):

    return render(request,'services/authenticated.html', {})


def services(request):

    return render(request, 'services/services.html', {})


def music_production(request):
    form = Music_ProductionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = Music_ProductionForm()

    context = {'form':form}
    return render(request, 'services/music_production.html', context)


def short_course(request):
    form = Short_CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = Short_CourseForm()
    context = {'form':form}
    return render(request, 'services/short_course.html',context)

def studio_session(request):
    form = Studio_SessionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = Studio_SessionForm()
    context = {'form':form}
    return render(request, 'services/studio_session.html',context)

def comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CommentForm()
    context = {'form':form}
    return render(request, 'services/make_a_comment.html', context)
