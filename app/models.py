from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
 
class blog(models.Model):
    admin=models.ForeignKey('auth.User')
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=200)
    text = models.CharField()
    date=models.DateTimeField(default=timezone.now())
