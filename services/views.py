
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from datetime import datetime
from django.shortcuts import render, redirect
from services.forms import Short_CourseForm, Music_ProductionForm, CommentForm,Studio_SessionForm
from coelibStudio.email_info import EMAIL_HOST_USER, ADMIN_EMAIL

def home(request):

    return render(request,'services/authenticated.html', {})


def services(request):

    return render(request, 'services/services.html', {})


def music_production(request):
    form = Music_ProductionForm(request.POST or None)
    if form.is_valid():
        form.save(commit = False)
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        booked_as = request.POST['booked_as']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        recepient_email = request.POST['email']
        message = full_name+' is requesting for music producion as '+booked_as+' from '+start_date+' to '+end_date+' your are requested to get in touch with him/her on '+phone_number+' or '+recepient_email+' . Thank you.'
        subject = 'Music Studio Session'
        sender = EMAIL_HOST_USER
        send_mail(subject,message,sender,[ADMIN_EMAIL],fail_silently=False)
        form.save()
        form = Music_ProductionForm()
    context = {'form':form}
    return render(request, 'services/music_production.html', context)


def short_course(request):
    form = Short_CourseForm(request.POST or None)
    if form.is_valid():
        form.save(commit = False)
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        course = request.POST['course']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        recepient_email = request.POST['email']
        message = full_name+ ' is requesting to enroll to  '+course+' course a from '+ start_date+' to '+end_date+' your are requested to get in touch with him/her on '+phone_number+' or '+recepient_email+' . Thank you.'
        subject = 'Music Course Enrollment'
        sender = EMAIL_HOST_USER
        send_mail(subject,message,sender,[ADMIN_EMAIL],fail_silently=False)
        form.save()
        form = Short_CourseForm()
    context = {'form':form}
    return render(request, 'services/short_course.html',context)

def studio_session(request):
    form = Studio_SessionForm(request.POST or None)
    if form.is_valid():
        form.save(commit = False)
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        booked_as = request.POST['booked_as']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        recepient_email = request.POST['email']
        message = full_name+' is requesting for studio session as a '+booked_as+' from '+start_date+' to '+end_date+ ' your are requested to get in touch with him/her on '+ phone_number+' or '+ recepient_email+'. Thank you.'
        print(message)
        subject = 'Studio Session'
        sender = EMAIL_HOST_USER
        send_mail(subject,message,sender,[ADMIN_EMAIL],fail_silently=False)
        form.save()
        form = Studio_SessionForm()
    context = {'form':form}
    return render(request, 'services/studio_session.html',context)

def comment(request):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        name = request.POST['name']
        recepient_email = request.POST['email']
        sender = EMAIL_HOST_USER
        comment = request.POST['comment']
        send_mail(name,comment,sender,[recepient_email],fail_silently=False)
        form.save(commit = False)
        form = CommentForm()        
    context = {'form':form}
    return render(request, 'services/make_a_comment.html', context)
