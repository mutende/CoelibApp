from services.forms import HireProducerForm, StudioSessionForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from services.models import HireProducer
from django.contrib import messages
from datetime import datetime

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
    #search for this month
    year = datetime.now().year
    month = datetime.now().month
    today = datetime.now()

    producers_schedule = HireProducer.objects.filter(hire_date__gte=today).filter(hire_date__year=year).filter(hire_date__month=month).order_by('-hire_date')
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
