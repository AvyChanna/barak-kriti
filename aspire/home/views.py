from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from aspire.home.models import Book, Course, Department, Novel, Video
from django.conf import settings


def index(request):
    return HttpResponseRedirect("accounts/login")


def home(request):
    d = Department.objects.all()
    return render(request, "home/index.html", {'depts':d})

# def courses(request):
#     request.GET.get()
#     c = Course.objects.filter(department__name=request.data)
def departments(request, slug):
    d = get_object_or_404(Department, slug=slug)
    c = Course.objects.filter(department=d)
    return render(request, 'department/index.html', {'dept': d, "courses":c})