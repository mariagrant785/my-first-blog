from django.shortcuts import render
from .models import Section
from .models import Project
# Create your views here.

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'resume/section_list.html', {'sections':sections})
