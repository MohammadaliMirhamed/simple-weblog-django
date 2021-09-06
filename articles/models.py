from django.conf import settings
from django.db import models
from django.utils import timezone

class Articles(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class GeneralSetting(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    facebook = models.CharField(max_length=300)
    instagram = models.CharField(max_length=300)
    twitter = models.CharField(max_length=300)

    def __str__(self):
        return self.title



class Menu(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=400)