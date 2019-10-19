from django.contrib import admin
from aspire.home import models

admin.register(models.Book)
admin.register(models.Course)
admin.register(models.Department)
admin.register(models.Novel)
admin.register(models.Tags)
admin.register(models.Video)
