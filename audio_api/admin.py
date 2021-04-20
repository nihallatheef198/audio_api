from django.contrib import admin
from . import models

admin.site.register(models.song)
admin.site.register(models.podcast)
admin.site.register(models.audio_book)
