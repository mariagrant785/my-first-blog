from django.db import models
from django.conf import settings

# Create your models here.

class Section(models.Model):
    section_name = models.CharField(max_length=20)
    # section will have related projects

    def __str__(self):
        return self.section_name

class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    section = models.ForeignKey(Section, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    company = models.CharField(max_length = 30)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
