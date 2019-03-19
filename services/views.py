from django.shortcuts import render
from services.forms import HireProducerForm

def home(request):

    return render(request,'services/authenticated.html', {})


def services(request):

    return render(request, 'services/services.html', {})


def studio_session(request):

    return render(request, 'services/studio_session.html', {})


def hire_producers(request):
    form = HireProducerForm()
    context = {'form': form}
    return render(request, 'services/hire_producers.html', context)
