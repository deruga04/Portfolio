import uuid
from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a title for the project')
    description = models.TextField()
    link = models.URLField()
    source = models.URLField(default='')
    image = models.ImageField(upload_to='img/projectthumbnails', default='img/banff_mountain.jpg')

    def __str__(self):
        return f'{self.name}: {self.description}'

class Photo(models.Model):
    PEOPLE = 'PE'
    LANDSCAPE = 'LA'
    CLOSE_UP = 'CL'
    FOOD = 'FD'
    MISC = 'MS'

    PHOTO_CATEGORY_CHOICES = (
        (PEOPLE, 'People'),
        (LANDSCAPE, 'Landscape'),
        (CLOSE_UP, 'Close-up'),
        (FOOD, 'Food'),
        (MISC, 'Misc'),
    )
    
    name = models.CharField(max_length=200, help_text='Enter a title')
    description = models.TextField()

    def __str__(self):
        return f'{self.name}({self.photo_category})' 

