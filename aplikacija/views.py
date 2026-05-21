from django.shortcuts import render
from django.views import View 

# Create your views here.
def pocetna(request):
  return render(request,"aplikacija/pocetna.html")

def juniori_view(request):
    return render(request, 'aplikacija/juniori.html')

def kadeti_view(request):
    # Ako budeš povlačio kadete iz baze, ovdje ćeš dodati query (npr. Kadeti.objects.all())
    return render(request, 'aplikacija/kadeti.html')

def povijest_kluba(request):
    return render(request, 'aplikacija/povijest.html')

def seniori_view(request):
    return render(request, 'aplikacija/seniori.html')

def izvjestaj_view(request):
    return render(request, 'aplikacija/izvjestaj.html')

def vijest1_view(request):
    return render(request, 'aplikacija/vijest1.html')

def vijest2_view(request):
    return render(request, 'aplikacija/vijest2.html')

def vijest3_view(request):
    return render(request, 'aplikacija/vijest3.html')

def sponzori_view(request):
    return render(request, 'aplikacija/sponzori.html')

