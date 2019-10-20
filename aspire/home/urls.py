from django.urls import path
from aspire.home import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'home/', views.home, name='home'),
    path(r'depts/<slug:dept>/course/<slug:sub>', views.courses, name="courses"),
    path(r'depts/<slug:slug>', views.departments, name='departments'),
    path(r'bookshare', views.bookshare, name='bookshare'),
    path(r'upload', views.share , name = 'share')
]
