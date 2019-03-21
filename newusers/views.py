from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from services.models import HireProducer,StudioSession
# Create your views here.


def index(request):

    return render(request, 'newusers/index.html', {})


def p_login(request):

    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in, WELCOME '+username+ '!')
            return redirect('producerpage')
        else:
            messages.success(request, 'Error during login, please retry')
            return redirect('producer_login')
    else:
        return render(request, 'newusers/p_login.html',{})


def producer(request):
    return render(request, 'newusers/producer_page.html',{})

def logout_user(request):
    logout(request)
    return redirect('index')

def hires(request):
    fixed_dates = HireProducer.objects.all()
    if(fixed_dates.count() < 1):
        messages.success(request, 'Sorry we currently have no hired producers')
    context = {'fixed_dates':fixed_dates}

    return render(request, 'newusers/producer_hires.html', context)

def studio_sessions(request):
    sessions_available = StudioSession.objects.all()
    if(sessions_available.count() < 1):
        messages.success(request, 'Sorry we currently have no active sessions')
    context = {'sessions_available':sessions_available}

    return render(request, 'newusers/studio_sessions.html', context)
