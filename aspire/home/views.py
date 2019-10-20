from django.shortcuts import render, get_object_or_404 , Http404
from django.http import HttpResponseRedirect, HttpResponse
from aspire.home.models import Department, Course, Video, Book
# from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt

def index(request):
    return HttpResponseRedirect("accounts/login")


def home(request):
    d = Department.objects.all()
    return render(request, "home/index.html", {'depts':d})



@xframe_options_exempt
def courses(request, dept, sub):
    d = get_object_or_404(Department, slug=dept)
    c = get_object_or_404(Course, slug=sub)
    if c.department.slug != dept:
        raise Http404
    v = Video.objects.filter(course=c)
    b = Book.objects.filter(course=c)
    return render(request, "course/index.html", {'dept':d, 'course':c, 'videos':v, 'books':b})


def departments(request, slug):
    d = get_object_or_404(Department, slug=slug)
    c = Course.objects.filter(department=d)
    return render(request, 'department/index.html', {'dept': d, "courses":c})
