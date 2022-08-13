from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add = True)