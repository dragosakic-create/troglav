from . import views
from django.urls import path

urlpatterns = [
    path("",views.pocetna),
    path('juniori', views.juniori_view, name='juniori'),
]




