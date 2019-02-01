from django.shortcuts import render
# Create your views here.


def home(request):

    return render(request,'services/authenticated.html', {})


def services(request):

    return render(request, 'services/services.html', {})


def music_production(request):

    return render (request, 'service/music_product.html')
