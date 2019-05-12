from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from services.models import Music_Production, Studio_Session, Comment,Short_Course

class UserAdmin(admin.ModelAdmin):
    
    list_filter =('date_joined','is_superuser','is_staff')


class SessionAdmin(admin.ModelAdmin):
    list_filter =('start_date','end_date','booked_as')
    list_display =('full_name','booked_as','start_date','end_date',)

class CommentAdmin(admin.ModelAdmin):
    list_filter =('comment_date',)
    fields =('name','email','comment',)
    list_display=('name','email','comment','comment_date',)
    
class ShortCoursesAdmin(admin.ModelAdmin):
    list_filter = ('course','start_date','end_date',)
    fileds= ('full_name','phone_number','email','course','start_date','end_date')
    list_display = ('full_name','phone_number','email','course','start_date','end_date')


# Register your models here.

admin.site.register(Music_Production,SessionAdmin)
admin.site.register(Studio_Session,SessionAdmin)
admin.site.register(Short_Course,ShortCoursesAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.unregister(Group)

