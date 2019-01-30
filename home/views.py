from django.shortcuts import render
from .projects import projects

def home(request):
  context = {
    'projects': projects 
  }
  return render(request, 'home/home.html', context)
