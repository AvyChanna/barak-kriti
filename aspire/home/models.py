from django.db import models
from django.conf import settings
from django.utils.text import slugify



class Department(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()
    slug = models.SlugField(max_length=50, unique=True, default="dept")

    def _get_unique_slug(self):
        '''
        In this method a unique slug is created
        '''
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Department.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

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
    author = models.CharField(max_length=100, blank=True)
    img = models.ImageField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    is_borrowed = models.BooleanField()

class Tags(models.Model):
    name = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)
