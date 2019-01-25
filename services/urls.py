from django.urls import path
from . import views


urlpatterns = [

    path('', views.services,  name='services'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_client,name='login_client'),
    path('home/', views.home, name='authenticated'),

]