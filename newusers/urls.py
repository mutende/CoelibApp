
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index,  name='index'),
    path('login/', views.p_login, name='producer_login'),
    path('producerpage/', views.producer, name="producerpage"),
    path('logout/', views.logout_user, name='logout'),
    path('services/', include('services.urls')),
    path('music/session', views.music_production_sessions, name="music_session"),
    path('studio/sessions/', views.studio_sessions, name="studio_sessions"),
    path('readcomments/', views.read_comments, name='read_comments'),
    path('music/classes/', views.enrolled_students, name="music_classes"),



]
