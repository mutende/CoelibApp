from django.db import models

class StudioSession(models.Model):
    BOOK_AS_CHOICES = (('Producer','Producer'),('Other','Other'))
    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=13)
    booked_as = models.CharField(max_length=20, choices=BOOK_AS_CHOICES, default='Other')
    start_date = models.DateField(auto_now=False)
    # starting_time = models.CharField(max_length=100)


class HireProducer(models.Model):
    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=13)
    producer_name= models.CharField(max_length=100)
    hire_date = models.DateField(auto_now=False)
    hire_time = models.TimeField(auto_now=False)
    duration_days = models.IntegerField(default=0)

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.CharField(max_length=500)
    comment_date = models.DateField(auto_now_add=True)
