from .models import *
from django.views.generic import *
from django.views.generic.edit import *
import json
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

# Allows navigation bar search feature in all pages
class SearchMixin(object):

	# Handle post requests
	def post(self, request):
		query = request.POST.get("search")

		if query:
			found = False

			people_list = []
			# Find in Faculties
			try:
				people_list.extend(Faculty.objects.filter(
					Q(firstname__istartswith=query) | Q(lastname__istartswith=query)
				))
			except ObjectDoesNotExist:
				pass

			# Find in Students
			try:
				people_list += Student.objects.filter(
					Q(firstname__istartswith=query) | Q(lastname__istartswith=query)
				).values()
			except ObjectDoesNotExist:
				pass

			# Find in Visiting Scholars
			try:
				people_list += VisitingScholar.objects.filter(
					Q(firstname__istartswith=query) | Q(lastname__istartswith=query)
				).values()
			except ObjectDoesNotExist:
				pass


			# Find in Paper
			paper_list = []
			try:
				paper_list += Paper.objects.filter(
					Q(title__icontains=query) | Q(author__icontains=query)
				).values()
			except ObjectDoesNotExist:
				pass
			
			found = (len(paper_list) > 0) or (len(people_list) > 0)

			# Return search result page rendered with variables
			return render(request, "app_coi/search_result.html", {
				'found': found, 
				'people_list': people_list, 
				'paper_list': paper_list,
			})

		else:
			return super(IndexView, self).get(request)

# http://www.columbia-coi.com/
class IndexView(SearchMixin, ListView):
	model = Featured
	template_name = 'app_coi/index.html'
	context_object_name = 'featured_list'
	queryset = model.objects.filter(order__gt=0).order_by("order")

# http://www.columbia-coi.com/about
class AboutView(SearchMixin, TemplateView):
	template_name = 'app_coi/about.html'

# http://www.columbia-coi.com/contact
class ContactView(SearchMixin, TemplateView):
	template_name = 'app_coi/contact.html'	

# http://www.columbia-coi.com/papers
class PaperListView(SearchMixin, ListView):
	model = Paper
	template_name = 'app_coi/papers.html'
	context_object_name = 'paper_list'
	queryset = model.objects.all()

	# Handle get request
	def get(self, request):
		# Search by title
		query = request.GET.get("title")
		if query:
			q = Q()
			for keyword in query.split():
				q = q & Q(title__icontains=keyword)
			
			paper_list = self.model.objects.filter(q)
			return render(request, "app_coi/paper_list.html", {'paper_list': paper_list})

		# Search by author
		elif request.GET.get("author"):
			query = request.GET.get("author")
			q = Q()
			for keyword in query.split():
				q = q & Q(author__icontains=keyword)

			paper_list = self.model.objects.filter(q)
			return render(request, "app_coi/paper_list.html", {'paper_list': paper_list})

		else:
			return super(PaperListView, self).get(request)


# http://www.columbia-coi.com/featured
class FeaturedView(SearchMixin, ListView):
	model = Featured
	template_name = 'app_coi/featured.html'
	context_object_name = 'featured_list'
	queryset = model.objects.all()


# http://www.columbia-coi.com/featured/[slug]
class FeaturedDetailView(SearchMixin, DetailView):
	model = Featured
	template_name = 'app_coi/featured_detail.html'
	context_object_name = 'featured'

	def get_context_data(self, **kwargs):
		context = super(FeaturedDetailView, self).get_context_data(**kwargs)
		# context['question_list'] = self.object.questions.all()
		return context



# http://www.columbia-coi.com/faculty
class FacultyView(SearchMixin, ListView):
	model = Faculty
	template_name = 'app_coi/faculty.html'
	context_object_name = 'people_list'
	queryset = model.objects.filter(category__in=["D", "A"]).order_by("-lastname")

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
				faculty_list = self.model.objects.filter(category__in=["D", "A"]).order_by("-lastname")
			elif "columbia" in category:
				faculty_list = self.model.objects.filter(category="C").order_by("lastname")
			elif "external" in category:
				faculty_list = self.model.objects.filter(category="E").order_by("lastname")

			return render(request, "app_coi/people_list.html", {'people_list': faculty_list})

		else:
			return super(FacultyView, self).get(request)
	

# http://www.columbia-coi.com/student
class StudentView(SearchMixin, ListView):
	model = Student
	template_name = 'app_coi/student.html'
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
			student_list = {}
			if "current" in request.GET["category"]:
				student_list = self.model.objects.filter(category="C").order_by("lastname")
			elif "alumni" in request.GET["category"]:
				student_list = self.model.objects.filter(category="A").order_by("lastname")

			return render(request, "app_coi/people_list.html", {'people_list': student_list})


		else:
			return super(StudentView, self).get(request)




# http://www.columbia-coi.com/scholar
class ScholarView(SearchMixin, ListView):
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




class EventView(SearchMixin, TemplateView):
	template_name = 'app_coi/event.html'



