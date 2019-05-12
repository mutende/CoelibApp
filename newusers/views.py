from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from services.models import Music_Production,Studio_Session,Comment,Short_Course
from django.contrib.auth.models import User
from datetime import datetime, date
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
            messages.success(request, 'Error during login, please retry with correct credentials')
            return redirect('producer_login')
    else:
        return render(request, 'newusers/p_login.html',{})


def producer(request):
    return render(request, 'newusers/producer_page.html',{})

def logout_user(request):
    logout(request)
    return redirect('index')


def hires(request):
    Users = User.objects.all()

    fromdate = request.GET.get('from')
    todate = request.GET.get('to')

    if fromdate == None or todate == None:
         fixed_dates = HireProducer.objects.all().order_by('-hire_date')[:5]
         fixed_date_count = HireProducer.objects.all().count()
         if fixed_date_count < 1:
             messages.success(request, 'There are no hired producer currently')
         elif fixed_date_count > 5:
            messages.success(request, 'There are '+ str(fixed_date_count) + ' hired producers but we are displaying the latest 5 hires')
    else:
        fromdate = datetime.strptime(fromdate, "%Y-%m-%d").date()
        todate = datetime.strptime(todate, "%Y-%m-%d").date()
        fixed_dates = HireProducer.objects.filter(hire_date__gte=fromdate).filter(hire_date__lte=todate)

        fromdt = str(fromdate)
        todt = str(todate)

        fixed_date_count = fixed_dates.count()

        if fixed_date_count < 1:
            messages.success(request, 'There are no hires for the period from '+ fromdt +' to '+todt)
        else:
            messages.success(request, 'Filtering hires from '+ fromdt +' to '+todt)


    context = {'fixed_dates':fixed_dates, 'Users':Users}
    return render(request, 'newusers/producer_hires.html', context)


#studio sessions
def studio_sessions(request):
    sessions_from = request.GET.get('from')
    sessions_to = request.GET.get('to')

    if sessions_from == None or sessions_to == None:
        count_sessions = Studio_Session.objects.all().count()
        sessions_available = Studio_Session.objects.all().order_by('-start_date')[:5]
        if count_sessions < 1:
            messages.success(request, 'There are no available sessions currently')
        elif count_sessions > 5:
            messages.success(request, 'There are a total of '+ str(count_sessions)+' sessions but we are showing the latest 5')
    else:
        sessions_from = datetime.strptime(sessions_from, "%Y-%m-%d").date()
        sessions_to = datetime.strptime(sessions_to, "%Y-%m-%d").date()
        sessions_available = Studio_Session.objects.filter(start_date__gte=sessions_from).filter(start_date__lte=sessions_to)
        fromdt = str(sessions_from)
        todt = str(sessions_to)
        if(sessions_available.count() < 1):
            messages.success(request, 'No Sessions available from '+ fromdt +' to '+todt)
        else:
            messages.success(request, 'Filtering Sessions from '+ fromdt +' to '+todt)

    context = {'sessions_available':sessions_available}
    return render(request, 'newusers/studio_sessions.html', context)

#music production 
def music_production_sessions(request):
    sessions_from = request.GET.get('from')
    sessions_to = request.GET.get('to')

    if sessions_from == None or sessions_to == None:
        count_sessions = Music_Production.objects.all().count()
        sessions_available = Music_Production.objects.all().order_by('-start_date')[:5]
        if count_sessions < 1:
            messages.success(request, 'There are no available sessions currently')
        elif count_sessions > 5:
            messages.success(request, 'There are a total of '+ str(count_sessions)+' sessions but we are showing the latest 5')
    else:
        sessions_from = datetime.strptime(sessions_from, "%Y-%m-%d").date()
        sessions_to = datetime.strptime(sessions_to, "%Y-%m-%d").date()
        sessions_available = Music_Production.objects.filter(start_date__gte=sessions_from).filter(start_date__lte=sessions_to)
        fromdt = str(sessions_from)
        todt = str(sessions_to)
        if(sessions_available.count() < 1):
            messages.success(request, 'No Sessions available from '+ fromdt +' to '+todt)
        else:
            messages.success(request, 'Filtering Sessions from '+ fromdt +' to '+todt)

    context = {'sessions_available':sessions_available}
    return render(request, 'newusers/music_production.html', context)

#enrolled student
def enrolled_students(request):
    sessions_from = request.GET.get('from')
    sessions_to = request.GET.get('to')

    if sessions_from == None or sessions_to == None:
        count_sessions = Short_Course.objects.all().count()
        students = Short_Course.objects.all().order_by('-start_date')[:5]
        if count_sessions < 1:
            messages.success(request, 'There are no students who have enrolled as per now')
        elif count_sessions > 5:
            messages.success(request, 'There are a total of '+ str(count_sessions)+' students but we are dispalying latest 5 who enrolled recently')
    else:
        sessions_from = datetime.strptime(sessions_from, "%Y-%m-%d").date()
        sessions_to = datetime.strptime(sessions_to, "%Y-%m-%d").date()
        students = Short_Course.objects.filter(start_date__gte=sessions_from).filter(start_date__lte=sessions_to)
        fromdt = str(sessions_from)
        todt = str(sessions_to)
        if(students.count() < 1):
            messages.success(request, 'No students who enrolled between '+ fromdt +' and '+todt)
        else:
            messages.success(request, 'Filtering students who enrolled between  '+ fromdt +' and '+todt)

    context = {'students':students}
    return render(request, 'newusers/music_classes.html', context)

def read_comments(request):
    comments = Comment.objects.all().order_by('-comment_date')[:10]
    count_comments = Comment.objects.all().count()
    if(comments.count() < 1):
        messages.success(request, 'Sorry there are no comments currently')
    elif count_comments > 10:
        count_comments = str(count_comments)
        messages.success(request, 'There are '+ count_comments + ' comments but we are showing the 10 latest comments')

    context = {'comments':comments, 'count_comments':count_comments}
    return render(request, 'newusers/read_comments.html', context)
