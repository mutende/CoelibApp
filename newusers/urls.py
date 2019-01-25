
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index,  name='index'),
    path('producer/', views.p_login, name='producer_login'),
    path('producerpage/', views.producer, name="producerpage"),
    path('logout/', views.logout_user, name='logout'),
    path('sessions/', views.sessions, name="sessions"),
    path('services/', include('services.urls')),


]