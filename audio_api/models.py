from django.db import models
from django.contrib.postgres.fields import ArrayField

class song(models.Model):
    name = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class podcast(models.Model):
    name = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100, blank=False)
    participants = ArrayField(models.CharField(max_length=100), size=10, null=True, blank=True, default=list)
    def __str__(self):
        return self.name

class audio_book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    narrator = models.CharField(max_length=100, blank=False)
    duration = models.PositiveIntegerField(blank=False)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
