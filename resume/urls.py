from django.urls import path
from . import views


urlpatterns = [path('', views.section_list, name='section_list'),
               path('sections/<str:section_name>/', views.project_list, name='section')]
