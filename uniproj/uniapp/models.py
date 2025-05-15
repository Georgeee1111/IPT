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
    

class University(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=500, blank=True)
    
    # Fields for filtering
    COURSE_LEVELS = [
        ('undergraduate', 'Undergraduate'),
        ('postgraduate', 'Postgraduate'),
        ('doctorate', 'Doctorate'),
    ]
    
    LOCATIONS = [
        ('cagayan_de_oro', 'Cagayan de Oro'),
        ('philippines', 'Philippines'),
        ('asia', 'Asia'),
    ]
    
    FIELDS_OF_STUDY = [
        ('computer_science', 'Computer Science'),
        ('engineering', 'Engineering'),
        ('business', 'Business'),
        ('medicine', 'Medicine'),
        ('arts', 'Arts & Humanities'),
    ]
    
    course_level = models.CharField(max_length=20, choices=COURSE_LEVELS, default='undergraduate')
    field_of_study = models.CharField(max_length=20, choices=FIELDS_OF_STUDY, default='computer_science')
    city = models.CharField(max_length=100, choices=LOCATIONS, default='cagayan_de_oro')
    
    def __str__(self):
        return self.name

    
