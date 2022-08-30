from django.db import models

# Create your models here.
class urlShortener(models.Model):
    longurl = models.CharField(max_length=255)
    shorturl = models.CharField(max_length=10, unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)