from django.db import models

class Music_Production(models.Model):
    class Meta:
        verbose_name_plural = 'Booked Music Production Sessions'
    BOOK_AS_CHOICES = (('Producer','Producer'),('Artist','Artist'))
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    booked_as = models.CharField(max_length=20, choices=BOOK_AS_CHOICES, default='Artist')
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)

class Studio_Session(models.Model):
    class Meta:
        verbose_name_plural = 'Booked Studio Sessions'

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    booked_as = models.CharField(max_length=8, default='Producer')
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)

class Short_Course(models.Model):
    class Meta:
        verbose_name_plural = 'Enrollment For Short Courses'

    CHOICES = (('Music Production','Music Production'),('Instruments','Instruments'))
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=20, choices=CHOICES, default='Music Production')
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.CharField(max_length=500)
    comment_date = models.DateField(auto_now_add=True)
