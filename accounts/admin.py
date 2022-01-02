from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.

class ProfileA(admin.ModelAdmin):
	list_display=('user', 'Department','Course','Phone_number')
	list_filter = ('Department','Course')
admin.site.register(Profile, ProfileA)