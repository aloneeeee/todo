from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=30)
    content=models.TextField(max_length=300)
    date_posted=models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

