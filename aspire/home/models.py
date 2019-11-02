from django.db import models
from django.conf import settings
from django.utils.text import slugify
from aspire.home.filerestrict import PdfFileField

class Department(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    img = models.ImageField()
    slug = models.SlugField(max_length=50, unique=True, default="dept", blank=False)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Department.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class Course(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True, default="sub", blank=False)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Department.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class ExtraLinks(models.Model):
    def __str__(self):
        return self.title
    url = models.URLField()
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Video(models.Model):
    def __str__(self):
        return self.title
    url = models.FileField()
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Book(models.Model):
    def __str__(self):
        return self.title
    pdf = PdfFileField()
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
    def __str__(self):
        return self.title
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    img = models.ImageField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    is_borrowed = models.BooleanField()

class Tag(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)
    courses = models.ManyToManyField(Course)


class Note(models.Model):
    def __str__(self):
        return self.title
    pdf = PdfFileField()
    title = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)