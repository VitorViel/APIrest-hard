from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=15)
    done = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
