from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from aspire.home.models import Department, Course, Video, Book


def index(request):
    return HttpResponseRedirect("accounts/login")


def home(request):
    d = Department.objects.all()
    return render(request, "home/index.html", {'depts':d})


def courses(request, dept, sub):
    d = get_object_or_404(Department, slug=dept)
    c = get_object_or_404(Course, slug=sub)
    if c.department.slug != dept:
        return HttpResponse("Invalid Course/Department", status=404)
    v = Video.objects.filter(course=c)
    b = Book.objects.filter(course=c)
    return render(request, "course/index.html", {'dept':d, 'course':c, 'videos':v, 'books':b})

def departments(request, slug):
    d = get_object_or_404(Department, slug=slug)
    c = Course.objects.filter(department=d)
    Course.objects.filter(slug)
    return render(request, 'department/index.html', {'dept': d, "courses":c})
