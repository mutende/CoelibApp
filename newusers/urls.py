
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index,  name='index'),
    path('producer/', views.p_login, name='producer_login'),
    path('producer page/', views.producer, name="producerpage"),
    path('logout/', views.logout_user, name='logout'),
    path('services/', include('services.urls')),
    path('hires/', views.hires, name="hires"),
    path('sessions/', views.studio_sessions, name="studio_sessions"),
    path('read comments/', views.read_comments, name='read_comments'),



]
