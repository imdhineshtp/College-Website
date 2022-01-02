from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Profile
from django.contrib.admin.widgets import AdminDateWidget


import re
# user registratio form
class CustomUserCreationForm(forms.Form):
    
    firstname = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={'class':'form-control text-center'}))
    lastname = forms.CharField(label='Last Name', max_length=50,widget=forms.TextInput(attrs={'class':'form-control text-center'}))
    username = forms.CharField(label = 'University Exam No', min_length=4, max_length=10,widget=forms.TextInput(attrs={'class':'form-control text-center'}))
    email = forms.EmailField(label='Email id', widget=forms.EmailInput(attrs={'class':'form-control text-center'}))
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs={'class':'form-control text-center'}))
    password2 = forms.CharField(label = 'Conform Password', widget=forms.PasswordInput(attrs={'class':'form-control text-center'}))

    def clean_firstname(self):
        firstname = self.cleaned_data['firstname']
        return firstname

    def clean_lastname(self):
        lastname = self.cleaned_data['lastname']
        return lastname
    
    def clean_username(self):
        username = self.cleaned_data['username']
        # au = '14'
        # if au==username[:2]:
        r = User.objects.filter(username = username)
        if r.count():
            raise ValidationError('username is already exists')
        return username
        # else:
            # raise ValidationError('Invalid University number')
        
    
    
    
    def clean_email(self):
        email = self.cleaned_data['email']
        r = User.objects.filter(email = email)
        if r.count():
            raise ValidationError('Email id is already exists')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        # checking password
        flag = 0
        while True:
            if (len(password1)<8):
                flag = -1
                break
            elif not re.search("[a-z]", password1):
                flag = -1
                break
            elif not re.search("[A-Z]", password1):
                flag = -1
                break
            elif not re.search("[0-9]", password1):
                flag = -1
                break
            elif re.search("\s", password1):
                flag = -1
                break
            elif not re.search("[_@#$%^&!]", password1):
                flag = -1
                break
            else:
                flag = 0
                break
        if flag == 0:    
            if password1 and password2 and password1 != password2:
                raise ValidationError(' Passwords did not matching')
            return password2
        else:
            raise ValidationError(' Password is not strong. Atleast it contain more then 8 characters with One Capital letter, One Small letter, One Number, One Special Character')
    
    def save(self, commit = True):
        user = User.objects.create_user(
    username = self.cleaned_data['username'],
    first_name=self.cleaned_data['firstname'],
    last_name=self.cleaned_data['lastname'],
    email=self.cleaned_data['email'],
    password=self.cleaned_data['password1']
)

        return user
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'email':forms.TextInput(attrs={'class':'form-control text-center', 'type':'email'}),
            'first_name':forms.TextInput(attrs={'class':'form-control text-center'}),
            'last_name':forms.TextInput(attrs={'class':'form-control text-center'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'Date_Of_Birth':forms.DateInput(attrs={'class':'form-control text-center', 'type':'date'}),
            'Department':forms.Select(attrs = {'class':'form-control text-center'}),
            'Phone_number':forms.TextInput(attrs = {'class':'form-control text-center'}),
            'Age':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Course':forms.TextInput(attrs = {'class':'form-control text-center'}),
            'Guard':forms.TextInput(attrs = {'class':'form-control text-center'}),
            # 'University_Exam_No':forms.TextInput(attrs={'class':'form-control'}),
            'Aadhar':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Gender':forms.Select(attrs = {'class':'form-control text-center'}),

            'Permanent_Address':forms.Textarea(attrs = {'class':'form-control  rounded ', 'rows':3, 'cols':3}),
            'Per_Taluk':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Per_Pin_Code':forms.NumberInput(attrs = {'class':'form-control text-center'}),
            'Per_State':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Per_Dist':forms.TextInput(attrs={'class':'form-control text-center'}),

            'Address':forms.Textarea(attrs = {'class':'form-control rounded','rows':3, 'cols':3}),
            'Taluk':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Pin_Code':forms.NumberInput(attrs = {'class':'form-control text-center'}),
            'State':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Dist':forms.TextInput(attrs={'class':'form-control text-center'}),

            'Image':forms.FileInput(attrs={'class':'form-control text-center', 'multiple':True}),
            'Sign':forms.FileInput(attrs={'class':'form-control text-center', 'multiple':True}),
        }
class profileupdateform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'Date_Of_Birth':forms.DateInput(attrs={'class':'form-control text-center', 'type':'date'}),
            'Department':forms.Select(attrs = {'class':'form-control text-center'}),
            'Guard':forms.TextInput(attrs = {'class':'form-control text-center'}),
            'Phone_number':forms.TextInput(attrs = {'class':'form-control text-center'}),
            'Age':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Course':forms.TextInput(attrs = {'class':'form-control text-center'}),
            # 'University_Exam_No':forms.TextInput(attrs={'class':'form-control'}),
            'Aadhar':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Gender':forms.Select(attrs = {'class':'form-control text-center'}),
            

            'Permanent_Address':forms.Textarea(attrs = {'class':'form-control  rounded ', 'rows':3, 'cols':3}),
            'Per_Taluk':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Per_Pin_Code':forms.NumberInput(attrs = {'class':'form-control text-center'}),
            'Per_State':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Per_Dist':forms.TextInput(attrs={'class':'form-control text-center'}),

            'Address':forms.Textarea(attrs = {'class':'form-control rounded','rows':3, 'cols':3}),
            'Taluk':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Pin_Code':forms.NumberInput(attrs = {'class':'form-control text-center'}),
            'State':forms.TextInput(attrs={'class':'form-control text-center'}),
            'Dist':forms.TextInput(attrs={'class':'form-control text-center'}),

            'Image':forms.FileInput(attrs={'class':'form-control text-center'}),
            'Sign':forms.FileInput(attrs={'class':'form-control text-center'}),
        }


