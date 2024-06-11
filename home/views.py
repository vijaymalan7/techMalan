from django.shortcuts import render ,redirect
# from .models import TeamMember
from .models import *

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    members = TeamMember.objects.all()
    return render(request, 'index.html',{'members':members})

def contactus(request):
    return render(request,'contactus.html')


def internship(request):
    Interntype = Internship.objects.all()
    return render(request,'internships.html',{'Interntype':Interntype})

def loginsignup(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        # phone=request.POST.get('uphone')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Email already exist.")
            return redirect('/login-signup/')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            )
    
        user.set_password(password)
        user.save()

        messages.info(request,'Account created Successfully')
        return redirect('/login-signup/')

    return render(request,'login-signup.html')

def handleLogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Email')
            return redirect('/login-signup/')

        user = authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login-signup/')
        else:
            login(request,user)
            return redirect('/')


    return render(request,'login-signup.html')


def handleLogout(request):
    logout(request)
    return redirect('/login-signup/')

@login_required(login_url="/login-signup/")
def enrollnow(request):
    return render(request,'enrollme.html')
    

def internshipdetail(request):
    return render(request,'internship-detail.html')

def ourteam(request):
    members = TeamMember.objects.all()
    return render(request, 'our-team.html', {'members': members})
    # return render(request,'our-team.html')