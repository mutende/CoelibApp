from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.


def home(request):

    return render(request,'services/authenticated.html', {})


def services(request):

    return render(request, 'services/services.html', {})


def signup(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created Successful, enjoy our services')
            return redirect('authenticated')
    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'services/signup.html', context)


def login_client(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username= username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in, WELCOME!')
            return redirect('authenticated')
        else:
            messages.success(request, 'Error during login, please retry')
            return redirect('login_client')

    return render(request,'services/login.html',{})
