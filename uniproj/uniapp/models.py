from django.db import models 
from django.db.models.signals import pre_save 
from uniproj.utils import *
from django.contrib.auth.models import User 

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title

class TrainerRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()

    def __str__(self):
        return self.user.first_name

class CourseInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=250, null = True, blank = True)
    course_category = [
      ('development', 'Development'),
      ('development', 'Development'),
      ('development', 'Development'),
      ('development', 'Development'),
      ('development', 'Development'),
    ]
    
