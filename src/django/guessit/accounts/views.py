from django.shortcuts import render, redirect
from .forms import RegistrationForm, AuthenticationForm
from django.contrib.auth import login,logout
from random import randint,sample,shuffle
from .models import Movie

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request,'home.html',{'username':user})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request,'home.html',{'username':None})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html',{'username':form.cleaned_data['username']})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def home(request,us=None):
    return render(request,'home.html',{'username':us})

def profile(request):
    return render(request,'profile.html')

def play(request):
    contents={}
    if request.method == 'GET':
        pk=randint(1,8548)
        mvs=list(Movie.objects.all().values_list('title', flat=True)) 
        mv=Movie.objects.get(pk=pk)
        opts=[mv.title]+sample(mvs,3)
        shuffle(opts)
        opt1,opt2,opt3,opt4=opts
        contents={"p1":mv.p1,"p2":mv.p2,"p3":mv.p3,"points":100,"genre":"#######","year":"#######","cast":"#######","opt1":opt1,"opt2":opt2,"opt3":opt3,"opt4":opt4}
    return render(request,"game.html",contents)