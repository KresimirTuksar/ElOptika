from django.urls import path
from . import views

#URLs
app_name = 'skladiste_app'

urlpatterns = [
    path("skladiste/", views.skladiste, name='skladiste'),
    path("skladiste/novi_unos/", views.dodaj, name = 'novi_unos'),
    path("skladiste/dodaj_kategoriju/", views.dodaj_kategoriju, name = 'dodaj_kategoriju'),
    path("skladiste/uredi_artikl/<str:pk>/", views.uredi, name='uredi_artikl'),
    path("skladiste/obrisi_artikl/<str:pk>/", views.obrisi_artikl, name='obrisi_artikl'),
    path("skladiste/artikl_detalji/<str:pk>/", views.detalji, name='artikl_detalji'),
    path("skladiste/reorder_level/<str:pk>/", views.reorder_level, name='reorder_level'),
    path("skladiste/izdavanje/<str:pk>/", views.izdavanje, name='izdavanje'),
    path("skladiste/zaprimanje/<str:pk>/", views.zaprimanje, name='zaprimanje'),
    
    path("skladiste/history", views.skladiste_history, name='skladiste_history'),

]
