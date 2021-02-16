from django.db import models
from django.db.models import  Model
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.


#
class Kategorija(models.Model):
    ime = models.CharField(max_length=50, blank=True, null=True,)

    def __str__(self):
        return self.ime

class Skladiste(models.Model):
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE, blank=True, null=True )
    naziv = models.CharField(max_length=50, blank=True, null=True)
    kolicina = models.IntegerField(default=0, blank=True ,null=True)
    primljena_kolicina = models.IntegerField(default=0, blank=True ,null=True)
    zaprimio = models.CharField(max_length=50, blank=True, null=True)
    izdana_kolicina = models.IntegerField(default=0, blank=True ,null=True)
    izdao = models.CharField(max_length=50, blank=True, null=True)
    izdano_na = models.CharField(max_length=50, blank=True, null=True)
    kreirao = models.CharField(max_length=50, blank=True, null=True)
    zaduzio = models.ManyToManyField(User, related_name='users', blank = True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True) #kada naručiti
    zadnje_osvjezeno = models.DateField(auto_now=True, auto_now_add=False)
    export_to_CSV = models.BooleanField(default=False) #export u csv format

    def __str__(self):
        return self.naziv


class SkladisteHistory(models.Model):
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    naziv = models.CharField(max_length=50, blank=True, null=True)
    kolicina = models.IntegerField(default=0, blank=True ,null=True)
    primljena_kolicina = models.IntegerField(default=0, blank=True ,null=True)
    zaprimio = models.CharField(max_length=50, blank=True, null=True)
    izdana_kolicina = models.IntegerField(default=0, blank=True ,null=True)
    izdao = models.CharField(max_length=50, blank=True, null=True)
    izdano_na = models.CharField(max_length=50, blank=True, null=True)
    zaduzio = models.ManyToManyField(User, related_name='skladisteh_zaduzio', blank = True)
    kreirao = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True) #kada naručiti
    zadnje_osvjezeno = models.DateField(auto_now=False, auto_now_add=False, null=True)
    

    def __str__(self):
        return self.naziv