from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import *
# Register your models here.

# custom admin panel
# class carouselA(admin.ModelAdmin):
# 	list_display=('Department', 'date_created', 'id')
# 	list_filter = ('Department',)

# class courseA(admin.ModelAdmin):
#     list_display = ('Department_name', 'Course_type')
#     list_filter = ('Department_name','Course_type')

admin.site.register(departments)
admin.site.register(revaluation)
admin.site.register(universityExam)
admin.site.register(department_details)
admin.site.register(course)
admin.site.register(carousel)

# @admin.register(Subject)
# class SubjectAdmin(ImportExportModelAdmin):
    # pass


admin.site.site_header = "Government Arts College, Paramakudi"
admin.site.site_title = "Admin"
admin.site.index_title = "GAC"
