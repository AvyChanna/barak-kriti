from django.urls import path
from aspire.home import views

urlpatterns = [
    path(r'', views.index, name='index'),
]
