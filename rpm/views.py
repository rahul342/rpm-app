from django.shortcuts import render_to_response, redirect
from models import *
from django.contrib import auth
from django.http import Http404, HttpResponse
from datetime import date, time, datetime
import json

def save_sleep_journal(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            patient = Patient.objects.get(email=email)
            today_date = date.today()
            sleep_journal_entry = SleepJournalEntry.objects.get_or_create(patient=patient, record_date = today_date)[0]
            q1 =  map(int, request.POST['q1'].split(":"))
            sleep_journal_entry.q1 = time(hour=q1[0], minute=q1[1])
            sleep_journal_entry.q2 = bool(int(request.POST['q2']))
            sleep_journal_entry.q3 = int(float(request.POST['q3']))
            sleep_journal_entry.q4 = bool(int(request.POST['q4']))
            sleep_journal_entry.q5 = int(float(request.POST['q5']))
            sleep_journal_entry.q6 = bool(int(request.POST['q6']))
            sleep_journal_entry.q7 = int(float(request.POST['q7']))
            sleep_journal_entry.save()
        except Exception, e:
            print e
            return HttpResponse('error')
        return HttpResponse('success')
    return HttpResponse("error")

def save_blood_pressure(request):
    if request.method == "POST":
        try:
            email = request.POST['email']
            patient = Patient.objects.get(email=email)
            for reading_data in json.loads(request.POST['data']):
                reading_date, reading = reading_data.split("|") 
                reading_date = datetime(**dict((zip(['year', 'month', 'day', 'hour', 'minute', 'second'], map(int, reading_date.split(":"))))))
                bp_entry = BloodPressureData.objects.get_or_create(patient=patient, reading_date=reading_date)[0]
                reading = map(int, reading.split(":"))
                bp_entry.sys = reading[0]
                bp_entry.dia = reading[1]
                bp_entry.pul = reading[2]
                bp_entry.save()
        except Exception, e:
            print e
            return HttpResponse('error')
        return HttpResponse('success')
    return HttpResponse("error")

#def home(request):
#    return render_to_response('login_signup.html')
#
#def login(request):
#    if request.method == 'GET':
#        if request.user.is_authenticated():
#            return render_to_response('index.html')
#        else:
#            return render_to_response('login_signup.html')
#    elif request.method == 'POST':
#        user = auth.authenticate(email=request.POST['email'], password=request.POST['password'])
#        if user is not None:
#            auth.login(request, user)
#            return render_to_response('index.html')
#        else:
#            return render_to_response("login_signup.html", dict(login_msg="Incorrect username or password"))
#
#def signup(request):
#    if request.method == "POST":
#        email = request.POST['email']
#        if user_exists(email):
#            return render_to_response("login_signup.html", dict(signup_msg="Email already exists."))
#        user = create_user(email, request.POST['password1'])
#        user.first_name = request.POST['name']
#        user.save()
#        return render_to_response("login_signup.html", dict(login_msg="Login using your email & password"))
#    else:
#        raise Http404()
#    
#def save_sleep_journal(request):
#    if request.method == "POST":
#        if request.user.is_authenticated():
#            ques_num = request.POST['ques_num']
#            journal_entry = SleepJournalEntry.objects.get_or_create(user=request.user, entry_date=date.today())[0]
#            setattr(journal_entry, ques_num, request.POST[ques_num])
#            journal_entry.save()
#            return HttpResponse("success")
#        else:
#            return HttpResponse("user_not_found")
#    else:
#        raise Http404()
#    
#def logout(request):
#    auth.logout(request)
#    return redirect('/')