from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    

class SleepJournalEntry(models.Model):
    patient = models.ManyToManyField(Patient)
    record_date = models.DateField()
    q1 = models.TimeField(null=True)
    q2 = models.NullBooleanField(null=True)
    q3 = models.PositiveSmallIntegerField(null=True)
    q4 = models.NullBooleanField(null=True)
    q5 = models.PositiveSmallIntegerField(null=True)
    q6 = models.NullBooleanField(null=True)
    q7 = models.PositiveSmallIntegerField(null=True)
    
class BloodPressureData(models.Model):
    patient = models.ManyToManyField(Patient)
    reading_date = models.DateTimeField()
    sys = models.FloatField(null=True)
    dia = models.FloatField(null=True)
    pul = models.FloatField(null=True)
    
    
    
    