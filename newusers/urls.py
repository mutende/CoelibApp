
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index,  name='index'),
    path('producer/', views.p_login, name='producer_login'),
]