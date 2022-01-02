from django.urls import path,re_path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views



urlpatterns=[
    re_path(r'^$', views.login, name='login'),
    re_path(r'^profile/$', views.student_page, name = 'student'),
    re_path(r'^register/$', views.register, name = 'register'),
    re_path(r'^logout/$', views.logout, name = 'logout'),
    re_path(r'^reset/$', views.reset, name = 'reset'),
    re_path(r'^editprofile/$', views.editpro, name = 'editprofile'),
    re_path(r'^fines/$', views.fines, name = 'fines'),
    re_path(r'^revalue/$', views.revaluate, name = 'revalue'),
    path('student/<str:uid>/', views.viewprofile, name = "Profiles"),
    re_path(r'^payment/$', views.paymentinterface, name = 'pay'),
    path('delete/<int:id>/', views.revaldelete, name = "revaldelete"),
    path('deleteall', views.revaldeleteall, name = "revaldeleteall"),

    path('aue',views.aue, name = 'aue'),
    path('auedelete/<int:id>/', views.auedelete, name = "auedelete"),
    path('auedeleteall', views.auedeleteall, name = "auedeleteall"),
    
    
    
]


 
 
