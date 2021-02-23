from django.urls import path
from . import views

#URLs
app_name = 'skladiste_app'

urlpatterns = [
    
#OPTIKA
    path("skladiste/optika/", views.listoptika, name='listoptika'),
    path("skladiste/optika/novi_unos", views.optika_dodaj, name='optika_dodaj'),
    path("skladiste/optika/dodaj_tip", views.dodaj_tip, name='dodaj_tip'),
    path("skladiste/optika/uredi/<str:pk>", views.optika_uredi, name='optika_uredi'),
    path("skladiste/optika/detalji/<str:pk>/", views.optika_detalji, name='optika_detalji'),
    path("skladiste/optika/izdaj/<str:pk>/", views.optika_izdaj, name='optika_izdaj'),
    path("skladiste/optika/obrisi/<str:pk>/", views.optika_obrisi, name='optika_obrisi'),
    path("skladiste/optika/reorder_level/<str:pk>/", views.optika_reorder_level, name='optika_reorder_level'),
    path("skladiste/optika/history/", views.optika_history, name='optika_history'),

#BAKAR
    path("skladiste/bakar/", views.listbakar, name='listbakar'),
    path("skladiste/bakar/novi_unos", views.bakar_dodaj, name='bakar_dodaj'),
    path("skladiste/bakar/dodaj_tip", views.dodaj_tip, name='dodaj_tip'),
    path("skladiste/bakar/uredi/<str:pk>", views.bakar_uredi, name='bakar_uredi'),
    path("skladiste/bakar/detalji/<str:pk>/", views.bakar_detalji, name='bakar_detalji'),
    path("skladiste/bakar/izdaj/<str:pk>/", views.bakar_izdaj, name='bakar_izdaj'),
    path("skladiste/bakar/obrisi/<str:pk>/", views.bakar_obrisi, name='bakar_obrisi'),
    path("skladiste/bakar/reorder_level/<str:pk>/", views.bakar_reorder_level, name='bakar_reorder_level'),
    path("skladiste/bakar/history/", views.bakar_history, name='bakar_history'),

#UTP
    path("skladiste/utp/", views.listutp, name='listutp'),
    path("skladiste/utp/novi_unos", views.utp_dodaj, name='utp_dodaj'),
    path("skladiste/utp/dodaj_tip", views.dodaj_tip, name='dodaj_tip'),
    path("skladiste/utp/uredi/<str:pk>", views.utp_uredi, name='utp_uredi'),
    path("skladiste/utp/detalji/<str:pk>/", views.utp_detalji, name='utp_detalji'),
    path("skladiste/utp/izdaj/<str:pk>/", views.utp_izdaj, name='utp_izdaj'),
    path("skladiste/utp/obrisi/<str:pk>/", views.utp_obrisi, name='utp_obrisi'),
    path("skladiste/utp/reorder_level/<str:pk>/", views.utp_reorder_level, name='utp_reorder_level'),
    path("skladiste/utp/history/", views.bakar_history, name='utp_history'),

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
    
    
    path("skladiste/history", views.skladiste_history, name='skladiste_history'),

]
