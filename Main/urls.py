from django.urls import path, re_path
from . import views

urlpatterns=[
    path('',views.index_view,name='index'),
    
    path('Department/<str:name>/',views.Department, name = "Department" ),
    re_path(r'^activities/$',views.activities, name  = 'activities'),
    re_path(r'^principal/$', views.prince, name = "principal"),
    re_path(r'^About/$', views.about, name = "about"),
    
       
]