from django.shortcuts import render_to_response
from models import SleepJournalEntry
from django.contrib import auth
from emailusernames.utils import user_exists
from emailusernames.utils import create_user
from django.http import Http404, HttpResponse
from datetime import date

def home(request):
    return render_to_response('login_signup.html')

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return render_to_response('index.html')
        else:
            return render_to_response('login_signup.html')
    elif request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return render_to_response('index.html')
        else:
            return render_to_response("login_signup.html", dict(login_msg="Incorrect username or password"))

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        if user_exists(email):
            return render_to_response("login_signup.html", dict(signup_msg="Email already exists."))
        user = create_user(email, request.POST['password1'])
        user.first_name = request.POST['name']
        user.save()
        return render_to_response("login_signup.html", dict(login_msg="Login using your email & password"))
    else:
        raise Http404()
    
def save_sleep_journal(request):
    if request.method == "POST":
        if request.user.is_authenticated():
            ques_num = request.POST['ques_num']
            journal_entry = SleepJournalEntry.objects.get_or_create(user=request.user, entry_date=date.today())[0]
            setattr(journal_entry, ques_num, request.POST[ques_num])
            journal_entry.save()
            return HttpResponse("success")
        else:
            return HttpResponse("user_not_found")
    else:
        raise Http404()