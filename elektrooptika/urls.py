from django.urls import path
from . import views

app_name = 'elektro'
urlpatterns = [
    path("",views.index, name="home"),
    path("reference/",views.reference, name="reference"),
    path("kontakt/",views.kontakt, name="kontakt"),
]
