from django.shortcuts import render, get_object_or_404, Http404
from aspire.home.models import Department, Course, Video, Book, Novel, Note
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 , Http404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NameForm

def index(request):
    return HttpResponseRedirect("accounts/login")

@login_required
def home(request):
    d = Department.objects.all()
    return render(request, "home/index.html", {'depts':d})

@login_required
def courses(request, dept, sub):
    c = get_object_or_404(Course, slug=sub)
    if c.department.slug != dept:
        raise Http404
    d = get_object_or_404(Department, slug=dept)
    t = c.tag_set.all()
    v = Video.objects.filter(course=c)
    b = Book.objects.filter(course=c)
    return render(request, "course/index.html",
                  {'dept':d, 'course':c, 'videos':v, 'books':b, "tags": t})

@login_required
def departments(request, slug):
    d = get_object_or_404(Department, slug=slug)
    c = Course.objects.filter(department=d)
    t = c.tag_set.all()
    return render(request, 'department/index.html', {'dept':d, "courses":c, "tags":t})

@login_required
def bookshare(request):
    n = Novel.objects.all()
    return render(request, "bookshare/index.html", {'novels':n})


@login_required
def share(request):
    if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'course/share.html', {'form': form} )

