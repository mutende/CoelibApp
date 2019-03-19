from django.contrib import admin
from services.models import Producer_Sessions, Music_Artist_Sessions,Hire_Producer

# Register your models here.

admin.site.register(Producer_Sessions)
admin.site.register(Music_Artist_Sessions)
admin.site.register(Hire_Producer)

