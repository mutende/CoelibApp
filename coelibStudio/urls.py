
from django.contrib import admin
from django.urls import path, include
from newusers import views

urlpatterns = [
    path('admin/logout/', views.logout_user),
    path('admin/', admin.site.urls),
    path('',include('newusers.urls')),
]