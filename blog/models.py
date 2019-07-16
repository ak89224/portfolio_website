from django.db import models
from django.utils import timezone

# Create your models here.

class blog(models.Model):
    blog_title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(null=True, default=timezone.now())
    body = models.TextField(default='None')
    thumbnail = models.ImageField(upload_to='images/')