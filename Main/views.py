from django.shortcuts import render
from .models import *


# Create your views here.
def index_view(request):
    dept = departments.objects.all()
    context = {'depts':dept}
    return render(request, 'home.html', context)

def Department(request, name):
	dept_detail = department_details.objects.get(name = name )
	
	depts_detail = departments.objects.get(name = name )
	course = depts_detail.course_set.all()
	carousel =  depts_detail.carousel_set.all()
	context = {'dept': dept_detail, 'courses':course, 'carousel':carousel}
	return render(request, "Departments/dept.html", context)


def about(request):
	return render(request, 'about.html')

def prince(request, *args, **kwargs):
    return render(request, "prince.html")

def activities(request, *args, **kwargs):
    return render(request, "activities.html")