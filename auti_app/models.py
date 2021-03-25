from django.db import models
from django.db.models.fields import CharField, DateField
import datetime

# Create your models here.
class Automobil(models.Model):
    ime  = models.CharField( max_length=50, verbose_name='Model', blank=False)
    marka = models.CharField(max_length=50, blank=False)
    tablica = models.CharField(max_length=10, blank=False)
    registracija_datum = models.DateField(verbose_name='Tehnički', null=False, blank=True)
    servis_datum = models.DateField(verbose_name='Zadnji servis',null=True, blank=True)
    servis_kilometri = models.IntegerField(verbose_name='Servis na', null=True, blank=True)
    do_servisa = models.IntegerField(blank=True)
    atest = models.DateField(verbose_name='Atest vatrogasnog aparata', blank=True)
    #kilometraža
    pocetna = models.IntegerField(default=0, blank=True, verbose_name='Kilometraža')
    zavrsna = models.IntegerField(default=0, blank=True,  verbose_name='Kilometraža')
    datum = models.DateField(auto_now=True, auto_now_add=False)
    relacija = CharField(max_length=100, blank = True)

    def __str__(self):
        return self.ime
    
    def istek_rege(self):
        return(self.registracija_datum - datetime.date.today()).days <= 10

    def istek_atest(self):
        return(self.atest - datetime.date.today()).days <= 10

        
class Kilometraza(models.Model):
    ime = models.CharField(max_length=50, blank = True)
    datum = models.DateField(auto_now=False, auto_now_add=True)
    pocetna = models.IntegerField(blank=True,null=True)
    zavrsna = models.IntegerField(blank=True, null=True)
    relacija = models.CharField(max_length=256, blank=True, null=True)
    dnevna_kilometraza = models.IntegerField(blank=True)
    zaduzio = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.automobil