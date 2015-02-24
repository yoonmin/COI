from django.contrib import admin
from .models import *

class FacultyAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'img', 'email', 'website', 'category')

class StudentAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'img', 'email', 'website')

class ScholarAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'img', 'email', 'website', 'category')	

class AlumniAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'img', 'email', 'website')	

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(CurrentStudent, StudentAdmin)
admin.site.register(VisitingScholar, ScholarAdmin)
admin.site.register(Alumni, AlumniAdmin)
