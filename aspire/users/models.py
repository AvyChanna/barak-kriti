from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from aspire.home.models import Tags

class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    recommends = models.ManyToManyField(Tags)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
