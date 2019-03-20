from django.shortcuts import render, redirect
from services.forms import HireProducerForm,StudioSessionForm
from django.contrib import messages

def home(request):

    return render(request,'services/authenticated.html', {})


def services(request):

    return render(request, 'services/services.html', {})


def studio_session(request):
    if request.method == 'POST':
        form = StudioSessionForm()
        if form.is_valid():
            form.save()
            messages.success(request,('Your booking is successful'))
            return redirect('studio_session')
        else:
            messages.success(request,('Error in forms please, correct and submit booking'))
            return redirect('studio_session')
    else:
        form = StudioSessionForm()

    context = {'form':form}
    return render(request, 'services/studio_session.html', context)


def hire_producers(request):
    if request.method == 'POST':
        form = HireProducerForm()
        if form.is_valid():
            form.save()
            messages.success(request,('Your booking is successful'))
            return redirect('hire_producers')
        else:
            messages.success(request,('Error in forms please, correct and submit booking'))
            return redirect('hire_producers')
    else:
        form = HireProducerForm()

    context = {'form':form}
    return render(request, 'services/hire_producers.html', context)
