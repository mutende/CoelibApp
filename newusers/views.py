from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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
            messages.success(request, 'You have been logged in, WELCOME!')
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

    messages.success(request, 'You have been logged out!')

    return redirect('index')


def sessions(request):

    return render(request,'newusers/sessions.html')
