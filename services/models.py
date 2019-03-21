from django.db import models

class StudioSession(models.Model):
    BOOK_AS_CHOICES = (('Producer','Producer'),('Other','Other'))
    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=13)
    booked_as = models.CharField(max_length=20, choices=BOOK_AS_CHOICES, default='Other')
    start_date = models.CharField(max_length=100)
    # starting_time = models.CharField(max_length=100)


class HireProducer(models.Model):


    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=13)
    producer_name= models.CharField(max_length=100)
    hire_date = models.CharField(max_length=100)
    hire_time = models.CharField(max_length=100)
    duration_days = models.IntegerField(default=0)
    # duration_hrs = models.IntegerField(default=0)
    # available_date= models.CharField(max_length=100,blank=True, null=True)
