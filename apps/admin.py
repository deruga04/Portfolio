from django.contrib import admin
from apps.models import Project
from apps.models import Photo

# Register your models here.
admin.site.register(Project)
admin.site.register(Photo)