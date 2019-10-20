from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from aspire.home.models import Book, Course, Department, Novel, Video
from django.conf import settings


def index(request):
    return HttpResponseRedirect("accounts/login")


def home(request):
    d = Department.objects.all()
    return render(request, "home/index.html", {'depts':d})