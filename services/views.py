from django.shortcuts import render
# Create your views here.


def home(request):

    return render(request,'services/authenticated.html', {})


def services(request):

    return render(request, 'services/services.html', {})


def music_production(request):

    return render(request, 'services/music_product.html', {})


def studio_session(request):

    return render(request, 'services/studio_session.html', {})


def hire_producers(request):

    return render(request, 'services/hire_producers.html', {});
