from django.urls import path
from . import views


urlpatterns = [

    path('', views.services,  name='services'),
    path('book_session/', views.music_production, name='music_production_session'),
    path('book_studio_session/', views.studio_session, name='studio_session'),
    path('hire_producer', views.hire_producers, name='hire_producers')

]