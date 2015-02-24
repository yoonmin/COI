from .models import *
from django.views.generic import *
import json
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.db.models import Q


class IndexView(TemplateView):
	template_name = 'app_coi/index.html'


class AboutView(TemplateView):
	template_name = 'app_coi/about.html'





class FacultyView(ListView):
	model = Faculty
	template_name = 'app_coi/faculty.html'
	context_object_name = 'people_list'
	queryset = model.objects.filter(category__in=["D", "AD"]).order_by("-lastname")

	def get(self, request):
		query = request.GET.get("q")
		if query:
			q = Q()
			for keyword in query.split():
				q = q & Q(firstname__istartswith=keyword) | Q(lastname__istartswith=keyword)
			
			people_list = self.model.objects.filter(q).order_by("lastname")
			return render(request, "app_coi/people_list.html", {'people_list': people_list})

		elif request.GET.get("category"):
			category = request.GET["category"]
			faculty_list = {}
			if "directors" in category:
				faculty_list = self.model.objects.filter(category__in=["D", "AD"]).order_by("-lastname")
			elif "columbia" in category:
				faculty_list = self.model.objects.filter(category="CFA").order_by("lastname")
			elif "external" in category:
				faculty_list = self.model.objects.filter(category="EFA").order_by("lastname")

			return render(request, "app_coi/people_list.html", {'people_list': faculty_list})

		else:
			return super(FacultyView, self).get(request)
	

class StudentView(ListView):
	model = CurrentStudent
	template_name = 'app_coi/student.html'
	context_object_name = 'people_list'
	queryset = model.objects.all().order_by("lastname")

	def get(self, request):
		query = request.GET.get("q")
		if query:
			q = Q()
			for keyword in query.split():
				q = q & Q(firstname__istartswith=keyword) | Q(lastname__istartswith=keyword)
			
			people_list = self.model.objects.filter(q).order_by("lastname")
			return render(request, "app_coi/people_list.html", {'people_list': people_list})

		else:
			return super(StudentView, self).get(request)








class ScholarView(ListView):
	model = VisitingScholar
	template_name = 'app_coi/scholar.html'
	context_object_name = 'people_list'
	queryset = model.objects.filter(category="C").order_by("lastname")


	def get(self, request):
		query = request.GET.get("q")
		if query:
			q = Q()
			for keyword in query.split():
				q = q & Q(firstname__istartswith=keyword) | Q(lastname__istartswith=keyword)
			
			people_list = self.model.objects.filter(q).order_by("lastname")
			return render(request, "app_coi/people_list.html", {'people_list': people_list})

		elif request.GET.get("category"):
			scholar_list = {}
			if "current" in request.GET["category"]:
				scholar_list = self.model.objects.filter(category="C").order_by("lastname")
			elif "past" in request.GET["category"]:
				scholar_list = self.model.objects.filter(category="P").order_by("lastname")

			return render(request, "app_coi/people_list.html", {'people_list': scholar_list})

		else:
			return super(ScholarView, self).get(request)




class AlumniView(ListView):
	model = Alumni
	template_name = 'app_coi/alumni.html'
	context_object_name = 'people_list'
	queryset = model.objects.all()

	def get(self, request):
		query = request.GET.get("q")
		if query:
			q = Q()
			for keyword in query.split():
				q = q & Q(firstname__istartswith=keyword) | Q(lastname__istartswith=keyword)
			
			people_list = self.model.objects.filter(q).order_by("lastname")
			return render(request, "app_coi/people_list.html", {'people_list': people_list})
			
		else:
			return super(AlumniView, self).get(request)






class EventView(TemplateView):
	template_name = 'app_coi/event.html'





# class FacultyView(TemplateView):
# 	template_name = 'app_coi/faculty.html'

