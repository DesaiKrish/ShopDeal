from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def signup1(request):
    return render(request, 'signup1.html')

def signup(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        psw = request.POST['psw']

        if len(username) > 15:
             messages.error(request, "Username too long")
             # messages.add_message(request, messages.INFO, 'Hello world.')
             return redirect('/')

        myuser = User.objects.create_user(username, email, psw,)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, "Your account has been created")
        return redirect('/')

    else:
        return HttpResponse("Not found")

def handlelogin(request):
    if request.method == 'POST':

        uname = request.POST['uname']
        loginpass = request.POST['loginpass']
        user = authenticate(username=uname, password=loginpass)

        if user is not None:
            login(request, user)

            return redirect('/shop')
        else:
            messages.success(request, "Invalid credentials. Please try again.")
            return redirect('/')



    return HttpResponse('404-Not found')









