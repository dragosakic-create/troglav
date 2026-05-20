from . import views
from django.urls import path

urlpatterns = [
    path("",views.pocetna, name='pocetna'),
    path('juniori', views.juniori_view, name='juniori'),
    path('kadeti', views.kadeti_view, name='kadeti'),
    path('povijest', views.povijest_kluba, name='povijest'),
    path('seniori', views.seniori_view, name='seniori'),
    path('izvjestaj', views.izvjestaj_view, name='izvjestaj'),
]




