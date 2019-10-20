from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
	return HttpResponseRedirect("accounts/login")


def home(request):
    return render(request, template_name="home/index.html")