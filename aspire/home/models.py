from django.db import models
from django.conf import settings



class Department(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Video(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Book(models.Model):
    pdf = models.FileField()
    title = models.CharField(max_length=300)
    BookTypeChoices = [
        ('Tutorial', 'Tutorial'),
        ('Test', 'Test Paper'),
        ('Notes', 'Notes'),
        ('Solution', 'Solution'),
    ]
    bookType = models.CharField(
        choices=BookTypeChoices,
        max_length=20
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
class Novel(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    img = models.ImageField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    is_borrowed = models.BooleanField()
    
class Tags(models.Model):
    courses = models.ManyToManyField(Course)
