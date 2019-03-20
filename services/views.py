from django.shortcuts import render, redirect
from services.forms import HireProducerForm,StudioSessionForm
from django.contrib import messages
from django.contrib.auth.models import User
from services.models import Hire_Producer

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
    print(Users)
    search_date = request.GET.get('doh')
    search_producer = request.GET.get('available')
    if search_producer == 'Admin':
        messages.success(request, 'If you select admin you will not be helped, please select other options')
    print(search_date)
    print(search_producer)

    #search
    producers_schedule = Hire_Producer.objects.all()
    print(producers_schedule)

    form = HireProducerForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = HireProducerForm()
    context = {'form':form,'Users':Users,'producers_schedule':producers_schedule}
    return render(request, 'services/hire_producers.html', context)
