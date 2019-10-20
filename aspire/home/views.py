from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


def index(request):
	return HttpResponseRedirect("accounts/login")