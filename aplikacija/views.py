from django.shortcuts import render
from django.views import View 

# Create your views here.
def pocetna(request):
  return render(request,"aplikacija/pocetna.html")
