from django.shortcuts import render, redirect, HttpResponse


from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

import datetime
from datetime import date
import random
import  sys

from .forms import ProfileForm, EditProfileForm, profileupdateform
from .models import Profile


def login(request):
    if not request.user.is_authenticated:    	
        if request.method == 'POST':
            userName = request.POST['username']
            passWord = request.POST['password']
            user = authenticate(username=userName, password=passWord)
            if user is not None:
                auth_login(request, user)
                # messages.info(request, f'{userName} is loged in!')
                return redirect('student')
                    
            else:
                    return HttpResponse('<h2>something went wrong</h2>')
        return render(request, 'login.html')
    else:
        return redirect('student')

def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url = 'login')
def student_page(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            
            if request.method == 'POST':
                value = request.POST['search']
                depend = request.POST['by']
                
                if depend == "Register Number":
                    userid = User.objects.get(username = value)
                    profile = Profile.objects.all().filter(user  = userid)
                elif depend == "Name":
                    name = User.objects.get(first_name = value)
                    profile = Profile.objects.all().filter(user = name)
                elif depend == "Aadhar Number":
                    profile = Profile.objects.all().filter(Aadhar = value)
                context = {'profiles': profile}
            else:

                allusersprofiles = Profile.objects.all()
                context = {'userprofile':allusersprofiles}
            return render(request, 'admin.html', context)
        else:
            current_user = request.user
            profile = Profile.objects.all().filter(user_id = current_user)
            print(current_user)
            context={'profile':profile}
            return render(request, 'stu_profile.html', context)
        
@login_required(login_url = 'login')
def viewprofile(request,uid):
    profiles = Profile.objects.all().filter(user_id = uid)
    context={'profile':profiles}
    return render(request,'viewprofile.html',context)


        

def get_userBasic(user):
    userinfo = User.objects.values('username', 'first_name', 'last_name')
    for user in userinfo:
        values = user
    
    return values
def register(request, *args, **kwargs):

    form = CustomUserCreationForm(request.POST or None)
    profile = ProfileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        
        
        if all((form.is_valid(), profile.is_valid())) :
            form = form.save()
            profiles = profile.save(commit = False)
            profiles.user = form
            profiles.save()
            messages.success(request, 'new user is create.')
            return redirect('login')
        else:
            print(form.errors)
            print(profile.errors)

            
            
            
    
    # form = CustomUserCreationForm()
    # profile = ProfileForm()

    context = {'form':form, 'profile':profile}
    return render(request, 'register.html', context )





@login_required(login_url = 'login')
def editpro(request):
    if request.user.is_authenticated:
        site_profile = Profile.objects.get(user = request.user)
        form = EditProfileForm(instance = request.user)
        # profileform = ProfileForm(instance = request.user)
        profileform = profileupdateform( instance = site_profile)
        if request.method == 'POST':
            form = EditProfileForm(request.POST or None, instance = request.user)
            profileform = profileupdateform( request.POST or None, request.FILES or None, instance=site_profile)
            if form.is_valid() and profileform.is_valid():
                user_form = form.save()
                custom_form = profileform.save(commit=False)
                custom_form.user = user_form
                custom_form.save()
                return redirect('student')
            else:
                print(form.errors)
                print(profileform.errors)
            
        
        context = {'profile': profileform,'form':form, 'path':request.path}
        print(request.user.id)
        return render(request,'editprofile.html', context )

@login_required(login_url = 'login')
def fines(request):
    if request.user.is_authenticated:
        path = request.path
        context ={'path':path}
        if request.method=='POST':
            return render(request, 'payment.html', context)
        else:
            return render(request, 'fines.html', context)

@login_required(login_url = 'login')
def paymentinterface(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            path = request.path
            context ={'path':path}
            return render(request, 'payment.html', context)

@login_required(login_url = 'login')
def revaluate(request):
    if request.user.is_authenticated:
        path = request.path
        
        current_user = request.user
        profile = Profile.objects.all().filter(user_id = current_user)
        context = {'path': path, 'profile':profile}
        
        
        return render(request, 'revaluate.html', context)        



def reset(request):
    return HttpResponse("<h1> bye bye </h1>")
