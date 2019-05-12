from django.urls import path
from . import views


urlpatterns = [

    path('', views.services,  name='services'),
    path('music/production', views.music_production, name='music_production'),
    path('studio/session/', views.studio_session, name='studio_session'),
    path('courses/', views.short_course, name='short_course'),
    path('make_comment/', views.comment, name='comment'),

]
