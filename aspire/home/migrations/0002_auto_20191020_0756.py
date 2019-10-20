# Generated by Django 2.2.6 on 2019-10-20 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(default='dept', unique=True),
        ),
        migrations.AddField(
            model_name='novel',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='novel',
            name='owner',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]