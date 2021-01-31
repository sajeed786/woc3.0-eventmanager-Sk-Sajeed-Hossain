from django.db import models
from django import forms

# Create your models here.
class Participant(models.Model):
    participant_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10)
    email_id = models.EmailField()
    registration_type = models.CharField(max_length=15)
    no_of_people = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.participant_name



class Event(models.Model):
    participants = models.ManyToManyField(Participant, blank=True)
    event_name = models.CharField(max_length=50)
    event_description = models.TextField(default='Default event description')
    venue = models.CharField(max_length=60, default='online')
    event_poster_link = models.URLField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    registration_end_date = models.DateField()
    registration_end_time = models.TimeField()
    host_emailid = models.EmailField() 
    host_password = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.event_name