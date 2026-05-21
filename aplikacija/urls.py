from . import views
from django.urls import path

urlpatterns = [
    path("",views.pocetna, name='pocetna'),
    path('juniori', views.juniori_view, name='juniori'),
    path('kadeti', views.kadeti_view, name='kadeti'),
    path('povijest', views.povijest_kluba, name='povijest'),
    path('seniori', views.seniori_view, name='seniori'),
    path('izvjestaj', views.izvjestaj_view, name='izvjestaj'),
    path('vijest1', views.vijest1_view, name='vijest1'),
    path('vijest2', views.vijest2_view, name='vijest2'),
    path('vijest3', views.vijest3_view, name='vijest3'),
    path('sponzori', views.sponzori_view, name='sponzori'),
]




