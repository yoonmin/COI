from django.contrib import admin
from .models import *

class FacultyAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'img', 'email', 'website', 'category')

class StudentAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'img', 'email', 'website', 'category')

class ScholarAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'img', 'email', 'website', 'category')	

class AlumniAdmin(admin.ModelAdmin):
	list_display = ('firstname', 'lastname', 'img', 'email', 'website')	

class FeaturedAdmin(admin.ModelAdmin):
	list_display = ('name', 'category', 'summary', 'cover', 'thumb')

class PaperAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'date')

admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(VisitingScholar, ScholarAdmin)
admin.site.register(Featured, FeaturedAdmin)
admin.site.register(Paper, PaperAdmin)
