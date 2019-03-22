from django.shortcuts import render, redirect
from services.forms import HireProducerForm, StudioSessionForm, CommentForm
from django.contrib import messages
from django.contrib.auth.models import User
from services.models import HireProducer

def home(request):

    return render(request,'services/authenticated.html', {})


def services(request):

    return render(request, 'services/services.html', {})


def studio_session(request):
    form = StudioSessionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = StudioSessionForm()

    context = {'form':form}
    return render(request, 'services/studio_session.html', context)


def hire_producers(request):
    Users = User.objects.all()
    number_of_producers = (User.objects.all().count())-1
    print(number_of_producers)
    print(Users)

    #search
    producers_schedule = HireProducer.objects.all()
    print(producers_schedule)

    form = HireProducerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = HireProducerForm()
    context = {'form':form,'Users':Users,'producers_schedule':producers_schedule, 'count':number_of_producers}
    return render(request, 'services/hire_producers.html', context)

def comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CommentForm()
    context = {'form':form}
    return render(request, 'services/make_a_comment.html', context)
