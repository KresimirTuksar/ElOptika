from django.db import models
from django.db.models.fields import CharField, DateField

# Create your models here.
class Automobil(models.Model):
    ime  = models.CharField(max_length=50, blank=False)
    marka =  models.CharField(max_length=50, blank=False)
    tablica = CharField(max_length=20, blank=False)
    registracija = models.DateField(null=True, blank=False)
    servis = models.DateField(null=True, blank=False)
    servis_kilometri = models.PositiveIntegerField(null=True, blank=False)

    def __str__(self):
        return self.ime


