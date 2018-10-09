from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a title for the project')
    description = models.TextField()
    link = models.URLField()

    def __str__():
        return f'{self.name}\n\n{self.description}'