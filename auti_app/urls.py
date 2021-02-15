from django.urls import path
from . import views

#URLs
app_name = 'auti_app'

urlpatterns = [
    path("lista", views.lista, name='lista'),
    path("dodaj_automobil", views.dodaj, name='dodaj_automobil'),
    path("uredi_automobil/<str:pk>/", views.uredi, name='uredi_automobil'),
    path('obrisi_automobil/<str:pk>/',views.obrisi, name='obrisi_automobil'),
]

