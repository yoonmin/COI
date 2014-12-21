from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(ListView):
	template_name = 'app_coi/index.html'
