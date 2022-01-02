from django.db import models
from accounts.models import *

class departments(models.Model):
    name = models.CharField(max_length = 30, primary_key = True, blank = True, default = None)
    img = models.ImageField(upload_to = "Departments", null = True)
    desc = models.CharField(max_length=150, null = True)

    def __str__(self):
        return self.name

class department_details(models.Model):
    name = models.OneToOneField(departments, on_delete=models.CASCADE, null = True)
    About = models.TextField(null = True)

    def  __str__(self):
        return self.name.name

class course(models.Model):
	COURSE = (
		('UG','UG'),
		('PG','PG'),
        ('M.Phil', 'M.Phil'),
        ('Ph.D','Ph.D')
		)
	Department_name = models.ForeignKey(departments, on_delete=models.CASCADE)
	Course_type = models.CharField(null=True, max_length=40, choices=COURSE, default = None)
	Course_name = models.CharField(null = True, max_length=80)
	Course_duration = models.CharField(null=True, max_length=30)

	def  __str__(self):
		return self.Department_name.name

class carousel(models.Model):
	Department = models.ForeignKey(departments,on_delete=models.CASCADE)
	Image = models.ImageField(upload_to='Carousel', null = True)
	Img_title = models.CharField(max_length=30, null=True)
	Img_desc = models.CharField(max_length=500, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	

	def __str__(self):
		return self.Department.name

class Subject(models.Model):

	SEM = (
		('SEMESTER I','SEMESTER I'),
		('SEMESTER II','SEMESTER II'),
		('SEMESTER III','SEMESTER III'),
		('SEMESTER IV','SEMESTER IV'),
		('SEMESTER V','SEMESTER V'),
		('SEMESTER VI','SEMESTER VI'),
	)

	Department_name = models.ForeignKey(departments, on_delete = models.CASCADE, null = True)
	Semester = models.CharField(choices = SEM, null = True, default = None, max_length = 40)
	Subject_name = models.CharField(max_length = 50, null = True)
	Subject_code = models.CharField(max_length = 50, null = True)

	def __str__(self):
		return self.Subject_name


class revaluation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
	# department = models.ForeignKey(departments, on_delete=models.CASCADE,  null = True)
	name = models.CharField(max_length=30, null = True)
	code = models.CharField(max_length=30, null = True)
	marks = models.CharField(max_length = 30, null = True)

	def __str__(self):
		return self.name
	
class universityExam(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
	name = models.CharField(max_length=30, null = True)
	code = models.CharField(max_length=30, null = True)
	practical = models.BooleanField(default = False, blank = True)
	price = models.IntegerField(default = None, null = True)

	def __str__(self):
		return self.name