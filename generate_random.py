import site, sys
#site.addsitedir('/home/ubuntu/.virtualenv/dg_production/lib/python2.7/site-packages/')

from django.core.management import setup_environ
from mas import settings
setup_environ(settings)

from rpm.models import *
import random, datetime

pat = Patient.objects.all()[0]
from_date = datetime.date(2013,1,1)
to_date = datetime.date.today()

bp_poss = [0, 1, 1, 1, 2, 1, 1, 2, 1, 1]

for date_delta in range((to_date - from_date).days):
    cur_date = from_date + datetime.timedelta(days=date_delta)
    sje_obj = SleepJournalEntry.objects.get_or_create(patient=pat, record_date = cur_date)[0]
    sje_obj.q1 = datetime.time(hour=random.randrange(24), minute=random.randrange(60))
    sje_obj.q2 = random.choice([True, False])
    sje_obj.q4 = random.choice([True, False])
    sje_obj.q6 = random.choice([True, False])
    sje_obj.q3 = random.randrange(6)
    sje_obj.q5 = random.randrange(6)
    sje_obj.q7 = random.randrange(6)
    sje_obj.save()

    for i in range(random.randrange(1, 5)):
        poss = random.choice(bp_poss)
        read_date = datetime.datetime(year=cur_date.year, month=cur_date.month, day=cur_date.day,
             hour=random.randrange(24), minute=random.randrange(60), second=random.randrange(60))
        bp_entry = BloodPressureData.objects.get_or_create(patient=pat, reading_date=read_date)[0]
        if poss == 0:
            bp_entry.sys = random.randrange(80, 95)
            bp_entry.dia = random.randrange(55, 60)
            bp_entry.pul = random.randrange(55, 60)
        elif poss == 1:
            bp_entry.sys = random.randrange(95, 135)
            bp_entry.dia = random.randrange(60, 90)
            bp_entry.pul = random.randrange(60, 95)
        elif poss == 2:
            bp_entry.sys = random.randrange(140, 155)
            bp_entry.dia = random.randrange(90, 105)
            bp_entry.sys = random.randrange(95, 110)
        bp_entry.save()
    print cur_date
