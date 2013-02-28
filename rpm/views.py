from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from emailusernames.utils import user_exists
from emailusernames.utils import create_user
from django.http import Http404

def home(request):
    return render_to_response('login_signup.html')

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return render_to_response('index.html')
        else:
            return render_to_response('login_signup.html')
    elif request.method == 'POST':
        user = authenticate(email=request.POST['email'], password=request.POST['password'])
        if user is not None:
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