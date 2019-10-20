from django.contrib import admin
from aspire.home import models

admin.site.register(models.Book)
admin.site.register(models.Course)
admin.site.register(models.Department)
admin.site.register(models.Novel)
admin.site.register(models.Tag)
admin.site.register(models.Video)
admin.site.register(models.ExtraLinks)
