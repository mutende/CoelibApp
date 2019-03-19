from django.db import models


class Producer_Sessions(models.Model):

    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=13)
    start_date = models.DateField()
    starting_time = models.TimeField()


class Music_Artist_Sessions(models.Model):

    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=13)
    start_date = models.DateField()
    starting_time = models.TimeField()


class Hire_Producer(models.Model):

    id = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=13)
    producer_name= models.CharField(max_length=100)
    hire_date = models.DateField()
    hire_time = models.TimeField()
    duration_days = models.IntegerField(default=0)
    duration_hrs = models.IntegerField(default=0)
    available_date= models.DateField()
