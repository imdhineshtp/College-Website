from django.db import models
from django.contrib.auth.models import User
from .validators import *
from Main.models import departments
# Create your models here.



class Profile(models.Model):
    # specified choices
    # DEPARTMENT_CHOICES = (
    # ("Department of Computer Science", "Department of Computer Science" ),
    # ("Department of Electronics", "Department of Electronics" ),
    # ("Department of Bio-Chemistry", "Department of Bio-Chemistry" ),
    # ("Department of Chemistry", "Department of Chemistry" ),
    # ("Department of Tamil", "Department of Tamil" ),
    # ("Department of English", "Department of English" ),
    # ("Department of Mathematics", "Department of Mathematics" ),
    # ("Department of Physics", "Department of Physics" ),
    # ("Department of Commerce", "Department of Commerce" ),
    # ("Department of Business Administration", "Department of Business Administration" ),
    # ("Department of Histroy", "Department of Histroy" ),
    # ("Department of Economics", "Department of Economics" ),
    # )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    COURSE_CHOICES = (
        ('Bachelor Degree', 'Bachelor Degree'),
        ('Master Degree', 'Master Degree'),
    )

    user = models.OneToOneField(User, on_delete = models.CASCADE) 
    Date_Of_Birth = models.DateField(null=True)
    Department = models.ForeignKey(departments, null= True, on_delete=models.CASCADE)
    Phone_number = models.CharField(unique=True, null=True,max_length=10)
    Age = models.CharField(null=True, max_length = 3)
    Guard = models.CharField(null = True, max_length=40)
    Course = models.CharField(null = True, max_length = 40)
    # University_Exam_No = models.CharField(null=True, max_length=10)
    Aadhar = models.CharField(null = True, max_length=12)
    Gender = models.CharField(null=True, max_length = 50, choices= GENDER_CHOICES, default=None)
    

    Permanent_Address = models.TextField(null=True)
    Per_Taluk = models.CharField(null=True, max_length = 30)
    Per_Pin_Code = models.CharField(null=True, max_length=6)
    Per_State = models.CharField(null=True, max_length=30)
    Per_Dist = models.CharField(null=True, max_length = 30)

    Address = models.TextField(null = True)
    Dist = models.CharField(null=True, max_length = 30)
    Taluk = models.CharField(null=True, max_length = 30)
    Pin_Code = models.CharField(null=True, max_length=6)
    State = models.CharField(null=True, max_length=30)

    Image = models.ImageField(upload_to='profiles', null = True, verbose_name = "", validators = [validProfile])
    Sign = models.ImageField(upload_to='Signs', null=True,verbose_name = "", validators = [validSign])

    def __str__(self):
        return self.user.first_name

