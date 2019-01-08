from django.shortcuts import render

# Create your views here.


def index(request):

    return render(request, 'newusers/index.html', {})


def p_login(request):

    return render(request, 'newusers/p_login.html',{})
