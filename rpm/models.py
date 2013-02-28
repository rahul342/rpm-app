from django.db import models
from django.contrib.auth.models import User

class SleepJournalEntry(models.Model):
    user = models.OneToOneField(User)
    entry_date = models.DateField() 
    q1 = models.CharField(blank=True, max_length=5)
    q2 = models.CharField(blank=True, max_length=10)
    q3 = models.PositiveSmallIntegerField(blank=True, null=True)
