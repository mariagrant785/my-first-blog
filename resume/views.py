from django.shortcuts import render
from .models import Section
from .models import Project
# Create your views here.

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'resume/section_list.html', {'sections': sections})


def project_list(request, section_name):
    projects = Project.objects.filter(section=section_name)
    return render(request, 'resume/section.html', {'projects': projects})