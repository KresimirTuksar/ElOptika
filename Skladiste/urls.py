from django.urls import path
from . import views

#URLs
app_name = 'skladiste_app'

urlpatterns = [
    

    path("skladiste/optika/", views.listoptika, name='listoptika'),
    path("skladiste/optika/novi_unos", views.optika_dodaj, name='optika_dodaj'),
    path("skladiste/optika/dodaj_tip", views.dodaj_tip, name='dodaj_tip'),
    path("skladiste/optika/uredi/<str:pk>", views.optika_uredi, name='optika_uredi'),
    path("skladiste/optika/detalji/<str:pk>/", views.optika_detalji, name='optika_detalji'),
    path("skladiste/optika/izdaj/<str:pk>/", views.optika_izdaj, name='optika_izdaj'),
    path("skladiste/optika/obrisi/<str:pk>/", views.optika_obrisi, name='optika_obrisi'),
    path("skladiste/optika/reorder_level/<str:pk>/", views.optika_reorder_level, name='optika_reorder_level'),

#############
    path("skladiste/", views.skladiste, name='skladiste'),
    path("skladiste/novi_unos/", views.dodaj, name = 'novi_unos'),
    path("skladiste/dodaj_kategoriju/", views.dodaj_kategoriju, name = 'dodaj_kategoriju'),
    path("skladiste/uredi_artikl/<str:pk>/", views.uredi, name='uredi_artikl'),
    path("skladiste/obrisi_artikl/<str:pk>/", views.obrisi_artikl, name='obrisi_artikl'),
    path("skladiste/artikl_detalji/<str:pk>/", views.detalji, name='artikl_detalji'),
    path("skladiste/reorder_level/<str:pk>/", views.reorder_level, name='reorder_level'),
    path("skladiste/izdavanje/<str:pk>/", views.izdavanje, name='izdavanje'),
    path("skladiste/zaprimanje/<str:pk>/", views.zaprimanje, name='zaprimanje'),
    path("skladiste/zaduzivanje/<str:pk>/", views.zaduzivanje, name='zaduzivanje'),
    path("skladiste/optika/history/", views.optika_history, name='optika_history'),
    
    path("skladiste/history", views.skladiste_history, name='skladiste_history'),

]
