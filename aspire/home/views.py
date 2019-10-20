
from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponseRedirect
from aspire.home.models import Department, Course, Video, Book, Novel, Note
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 , Http404
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
    return HttpResponseRedirect("accounts/login")

@login_required
def home(request):
    d = Department.objects.all()
    return render(request, "home/index.html", {'depts':d})



@login_required
def courses(request, dept, sub):
    d = get_object_or_404(Department, slug=dept)
    c = get_object_or_404(Course, slug=sub)
    if c.department.slug != dept:
        raise Http404
    v = Video.objects.filter(course=c)
    b = Book.objects.filter(course=c)
    n = Note.objects.filter(course =c)
    return render(request, "course/index.html", {'dept':d, 'course':c, 'videos':v, 'books':b , 'notes':n})


@login_required
def departments(request, slug):
    d = get_object_or_404(Department, slug=slug)
    c = Course.objects.filter(department=d)
    return render(request, 'department/index.html', {'dept': d, "courses":c})

@login_required
def bookshare(request):
    n = Novel.objects.all()
    return render(request, "bookshare/index.html", {'novels':n})

