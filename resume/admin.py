from django.contrib import admin
from .models import Section
from .models import Project

# Register your models here.
admin.site.register(Section)
admin.site.register(Project)