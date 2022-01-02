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
from Main.models import *
# Create your views here.


def logout(request):
    auth_logout(request)
    return redirect('login')

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
        return render(request, 'registration/login.html')
    else:
        return redirect('student')

def reset(request):
    return HttpResponse("<h1> bye bye </h1>")

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

    context = {'form':form, 'profile':profile}
    return render(request, 'register.html', context )





@login_required(login_url = 'login')
def editpro(request):
    if request.user.is_authenticated:
        site_profile = Profile.objects.get(user = request.user)
        form = EditProfileForm(instance = request.user)
    
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
        userdept = Profile.objects.values('Department').filter(user_id = current_user)
        for dept in userdept:
            departmentss = dept['Department']
        
        subs = Subject.objects.all().filter(Department_name = departmentss)


        if request.method == 'POST':
            sub_name = request.POST.get('subject_name')
            marks = request.POST.get('marks')

            subj = Subject.objects.values('Subject_code').filter(Subject_name = sub_name)
            for sub in subj:
                subcode = sub['Subject_code']
            print(subcode)
            if not revaluation.objects.filter(name = sub_name, code = subcode, user_id = current_user).exists():
                re = revaluation.objects.create(user = current_user, name = sub_name, code=subcode, marks = marks)
            
                
        revalue = revaluation.objects.all().filter(user = current_user)
        context = {'path': path, 'profiles':profile, 'subjects':subs, 'revaluation':revalue}
        
        
        return render(request, 'revaluate.html', context)        

@login_required(login_url = 'login')
def revaldelete(request,id):
    if request.user.is_authenticated:
        
        reval = revaluation.objects.get(pk = id)
        reval.delete()
        print(request.path)
        return redirect("revalue")

        
@login_required(login_url = 'login')
def revaldeleteall(request):
    if request.user.is_authenticated:
        revaluation.objects.filter(user = request.user).delete()
        
        return redirect('student')

@login_required(login_url = 'login')
def aue(request):
    if request.user.is_authenticated:
        path = request.path
        current_user = request.user
        profile = Profile.objects.all().filter(user_id = request.user)
        userdept = Profile.objects.values('Department').filter(user_id = request.user)
        for dept in userdept:
            departmentss = dept['Department']
        
        if request.method == "POST":
            sub_name = request.POST.get('subject_name')
            practical = request.POST.get('practical')
            print(practical)

            subj = Subject.objects.values('Subject_code').filter(Subject_name = sub_name)
            for sub in subj:
                subcode = sub['Subject_code']
            # print(subcode)
            if not universityExam.objects.filter(name = sub_name, code = subcode, user_id = current_user).exists():
                if practical == 'yes':
                    aue = universityExam.objects.create(user = current_user, name = sub_name, code=subcode, practical = True, price = 90)
                else:
                    aue = universityExam.objects.create(user = current_user, name = sub_name, code=subcode, practical = False, price = 75)
        
        subs = Subject.objects.all().filter(Department_name = departmentss)
        uni = universityExam.objects.all().filter(user_id = current_user)
        context = {'path': path, 'profiles':profile, 'subjects':subs, 'aue':uni}
        return render(request,'aue.html', context)

@login_required(login_url = 'login')
def auedelete(request,id):
    if request.user.is_authenticated:
        
        reval = universityExam.objects.get(pk = id)
        reval.delete()
        
        return redirect("aue")

        
@login_required(login_url = 'login')
def auedeleteall(request):
    if request.user.is_authenticated:
        universityExam.objects.filter(user = request.user).delete()
        
        return redirect('student')