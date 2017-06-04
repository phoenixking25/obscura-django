from django.shortcuts import render_to_response,redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
import hashlib
import urllib
import datetime
import json

from .models import userSchema, levelSchema
from .forms import GetInfo, GetAns
from django.views import generic
from django.views.generic.detail import DetailView
# Create your views here.

#decorator for authenticating the user is logged in or not
def loginRequired(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated():
            return redirect('login_view')
        return func(request,*args,**kwargs)
    return wrapper


def getid(request):
    return request.user.id

#if a user is logged in then it is redirected to index page if he/she tries to access login or index page
def check_authentication(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated():
            return redirect('/')
        return func(request,*args,**kwargs)
    return wrapper







def entry(request):
    return render(request,'entry.html')

#route for login the user

@loginRequired
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def team(request):
    return render(request,'team.html')



@check_authentication
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None:
        	login(request,user)              
        else:
            messages.warning(request,'Invalid username or password')
            return redirect('/obscura/auth/login')
    return render(request,'auth/login.html')





#route for registering the user
@check_authentication
def register_view(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            User.objects.get(username = username)
            messages.warning(request,'Username already exists')
            return render(request,'/auth/register.html')
        except:
            if ' ' in username:
                messages.warning(request,'No Spaces allowed in Username')
                return render(request,'auth/register.html')
            else:
                user = User.objects.create_user(first_name = fname,last_name = lname,username = username,email = email,password = password)
                new_user_profile = userSchema(user = user)
                new_user_profile.save()
                messages.success(request,'Successfully Registered')
                pk = new_user_profile.pk
                return redirect('/obscura/info/'+str(pk))
    return render(request,'auth/register.html')



@loginRequired
def logout_view(request):
    logout(request)
    return redirect('/obscura/auth/login')

def get_info(request,pk):
    info = get_object_or_404(userSchema, pk =pk)
    form = GetInfo(request.POST or None)
    if request.method == 'POST':
        
        if form.is_valid():
            info.college = form.cleaned_data['college']
            info.location = form.cleaned_data['location']
            info.phone = form.cleaned_data['phone']

            info.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'auth/info.html', {'form': form})

@loginRequired
def levelview(request):
    user_profile = get_object_or_404(userSchema,user = request.user)
    level_id  = user_profile.currlevel
    level = get_object_or_404(levelSchema, id = level_id)
    real_ans = level.ans
    form = GetAns(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user_ans = form.cleaned_data['ans']
            if user_ans == real_ans:
                user_profile.currlevel += 1
                user_profile.save()
    return render(request,
        'levelview.html',
         {'user_profile':user_profile, 'level':level, 'form':form})




"""
@loginRequired
def levelview(request  ,level_id):
    level = get_object_or_404(levelSchema, id = level_id)
    return render(request, 'levelview.html', {
        'level': level,
        })

@loginRequired
def getans(request, level_id):
    
    level = get_object_or_404(levelSchema, id = level_id)
    form = GetAns(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user_ans = form.cleaned_data['ans']
            if user_ans == level.ans:
                info.currlevel += 1
                return redirect('/obscura/level/'+str(level_id)+ '/' )

            else:
                messages.warning('Wrong Answer!')


                return redirect('/obscura/level/' +str(level_id)+ '/' )
    return redirect(request, 'levelview.html',{
        'level':level,
        'info':info,
        'form':form 
        })
            """
