from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_delete

class ExtraInfo(models.Model):
    user = models.OneToOneField(User)
    college = models.CharField(max_length=30)
    major = models.CharField(max_length=30)

# user = User.objects.get(username='asdfg')
# college = user.student.college

@receiver(post_delete, sender=ExtraInfo)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.user: # just in case user is not specified
        instance.user.delete()


class Departments(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField()

class Courses(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=100)
    dept_id = models.IntegerField()
    course_img = models.CharField(max_length=300)

class Videos(models.Model):
    url = models.CharField(max_length=300)
    course_id = models.IntegerField()

class Books(models.Model):
    url = models.CharField(max_length=300)
    course_id = models.IntegerField()
