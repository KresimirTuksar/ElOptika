from django.db import models
from django.db.models import  Model
from django.db.models.fields import CharField, DateTimeField, PositiveIntegerField
from django.contrib.auth.models import User
from django.forms.widgets import DateTimeInput

# Create your models here.


#
class Kategorija(models.Model):
    ime = models.CharField(max_length=50, blank=True, null=True,)

    def __str__(self):
        return self.ime

class Skladiste(models.Model):
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE, blank=True, null=True )
    naziv = models.CharField(max_length=50, blank=True, null=True)
    kolicina = models.PositiveIntegerField(default=0, blank=True ,null=True)
    primljena_kolicina = models.IntegerField(default=0, blank=True ,null=True)
    zaprimio = models.CharField(max_length=50, blank=True, null=True)
    izdana_kolicina = models.IntegerField(default=0, blank=True ,null=True)
    izdao = models.CharField(max_length=50, blank=True, null=True)
    izdano_na = models.CharField(max_length=50, blank=True, null=True)
    kreirao = models.CharField(max_length=50, blank=True, null=True)
    zaduzio = models.ManyToManyField(User,through = 'Zaduzenje')
    zaduzena_kolicina =models.IntegerField(default=0, blank=True ,null=True)
    datum_zaduzivanja = models.DateTimeField(auto_now=True, auto_now_add=False)
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
    kreirao = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True) #kada naručiti
    zadnje_osvjezeno = models.DateField(auto_now=False, auto_now_add=False, null=True)
    

    def __str__(self):
        return self.naziv

class Zaduzenje(models.Model):
    naziv = models.ForeignKey(Skladiste, on_delete=models.CASCADE)
    zaduzeno_na = models.ForeignKey(User, on_delete=models.CASCADE)
    
    

# novo, prepravljeno

class Alat(models.Model):
    inv_broj = PositiveIntegerField(unique=True, verbose_name='Inventurni broj')
    naziv = models.CharField(max_length=50, verbose_name='Naziv')
    proizvodjac = models.CharField(verbose_name='Proizvođač', max_length=50)
    sr_broj = models.CharField(verbose_name='Serijski broj', max_length=50)
    kreirao = models.CharField(max_length=50, blank=True, null=True)
    zaduzio = models.ForeignKey(User, verbose_name="Zaduži na", on_delete=models.CASCADE)
    datum_zaduzivanja = models.DateField(verbose_name='Zaduženo dana', auto_now=True, auto_now_add=False)
    zadnje_osvjezeno = models.DateField(verbose_name='Posljednje ažuriranje', auto_now=True, auto_now_add=False)
    export_to_CSV = models.BooleanField(default=False) #export u csv format

    def __str__(self):
        return self.naziv


class Materijal(models.Model):
    inv_broj = PositiveIntegerField(default=0, verbose_name='Inventurni broj')
    naziv = models.CharField(max_length=50, verbose_name='Naziv')
    kolicina = models.PositiveIntegerField(verbose_name='Količina')
    zaprimljena_kolicina = models.PositiveIntegerField(verbose_name='Zaprimljena količina')
    zaprimio = models.ForeignKey(User, verbose_name="Zaprimio", related_name='users', on_delete=models.CASCADE)
    izdana_kolicina = models.PositiveIntegerField(verbose_name='Izdana količina')
    izdao = models.CharField(max_length=50, blank=True, null=True)
    izdano_na = models.ForeignKey(User, verbose_name="Izdaj na", on_delete=models.CASCADE)
    radnja = models.CharField(max_length=50, verbose_name='Radnja')
    reorder_level = models.IntegerField(default=0, blank=True, null=True) #kada naručiti
    export_to_CSV = models.BooleanField(default=False) #export u csv format

    def __str__(self):
        return self.naziv


class TipKabela(models.Model):
    tip = models.CharField(max_length=50, verbose_name='Tip kabela')

    def __str__(self):
        return self.tip


class KabelOptika(models.Model):
    inv_broj = PositiveIntegerField(blank=True, null=True, verbose_name='Inventurni broj')
    naziv = models.CharField(max_length=50, verbose_name="Naziv", blank=True, null=True)
    proizvodjac = models.CharField(blank=True, null=True, verbose_name='Proizvođač', max_length=50)
    vlasnik = models.CharField(max_length=50, verbose_name="Vlasnik", blank=True, null=True,)
    tip_kabela = models.ForeignKey(TipKabela, verbose_name="Tip kabela", blank=True, null=True, on_delete=models.CASCADE)
    broj_niti = PositiveIntegerField(blank=True, null=True, verbose_name='Broj niti')
    metraza = models.IntegerField(default=0, blank=True, null=True,verbose_name='Ukupna metraža')
    izdana_metraza = models.PositiveIntegerField(blank=True, null=True, verbose_name='Izdano metara')
    izdano_na = models.ForeignKey(User, blank=True, null=True, verbose_name="Izdaj na", on_delete=models.CASCADE)
    izdao = models.CharField(max_length=50, blank=True, null=True)
    kreirao = models.CharField(max_length=50, blank=True, null=True)
    radnja = models.CharField(verbose_name='Radnja', max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True) #kada naručiti
    zadnje_osvjezeno = models.DateTimeField(verbose_name='Posljednje ažuriranje', auto_now=True, auto_now_add=False)
    export_to_CSV = models.BooleanField(default=False) #export u csv format

    def __str__(self):
        return self.naziv

class KabelOptikaHistory(models.Model):
    inv_broj = PositiveIntegerField(blank=True, null=True, verbose_name='Inventurni broj')
    naziv = models.CharField(max_length=50, verbose_name="Naziv", blank=True, null=True)
    proizvodjac = models.CharField(blank=True, null=True, verbose_name='Proizvođač', max_length=50)
    vlasnik = models.CharField(max_length=50, verbose_name="Vlasnik", blank=True, null=True,)
    tip_kabela = models.ForeignKey(TipKabela, verbose_name="Tip kabela", blank=True, null=True, on_delete=models.CASCADE)
    broj_niti = PositiveIntegerField(default=1, verbose_name='Broj niti')
    metraza = models.PositiveIntegerField(default=0,verbose_name='Ukupna metraža')
    izdana_metraza = models.PositiveIntegerField(blank=True, null=True, verbose_name='Izdano metara')
    izdano_na = models.ForeignKey(User, blank=True, null=True, verbose_name="Izdaj na", on_delete=models.CASCADE)
    izdao = models.CharField(max_length=50, blank=True, null=True)
    kreirao = models.CharField(max_length=50, blank=True, null=True)
    radnja = models.CharField(verbose_name='Radnja', max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True) #kada naručiti
    zadnje_osvjezeno = models.DateTimeField(verbose_name='Posljednje ažuriranje', auto_now=False, auto_now_add=False, null=True)
    export_to_CSV = models.BooleanField(default=False) #export u csv format

    def __str__(self):
        return self.naziv



class KabelBakar(models.Model):
    inv_broj = PositiveIntegerField(unique=True ,verbose_name='Inventurni broj')
    naziv = models.CharField(max_length=50,verbose_name="Naziv")
    proizvodjac = models.CharField(max_length=50, verbose_name='Proizvođač', blank=True, null=True)
    vlasnik = models.CharField(max_length=50, verbose_name="Vlasnik")
    tip_kabela = models.ForeignKey(TipKabela, verbose_name="Tip kabela", on_delete=models.CASCADE)
    broj_pari = PositiveIntegerField(verbose_name='Broj parica')
    metraza = models.PositiveIntegerField(verbose_name='Ukupna metraža')
    izdana_metraza = models.PositiveIntegerField(blank=True, null=True, verbose_name='Izdano metara')
    izdano_na = models.ForeignKey(User, blank=True, null=True, verbose_name="Izdaj na", on_delete=models.CASCADE)
    radnja = models.CharField(verbose_name='Radnja', max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True) #kada naručiti
    zadnje_osvjezeno = models.DateField(verbose_name='Posljednje ažuriranje', auto_now=True, auto_now_add=False)
    export_to_CSV = models.BooleanField(default=False) #export u csv format

    def __str__(self):
        return self.naziv

class KabelUtp(models.Model):
    inv_broj = PositiveIntegerField(unique=True, verbose_name='Inventurni broj')
    naziv = models.CharField(max_length=50, verbose_name="Naziv")
    proizvodjac = models.CharField(max_length=50, verbose_name='Proizvođač',blank=True, null=True)
    vlasnik = models.CharField(max_length=50, verbose_name="Vlasnik")
    tip_kabela = models.ForeignKey(TipKabela, verbose_name="Tip kabela", on_delete=models.CASCADE)
    metraza = models.PositiveIntegerField(verbose_name='Ukupna metraža')
    izdana_metraza = models.PositiveIntegerField(blank=True, null=True, verbose_name='Izdano metara')
    izdano_na = models.ForeignKey(User, verbose_name="Izdaj na", blank=True, null=True, on_delete=models.CASCADE)
    radnja = models.CharField(verbose_name='Radnja', max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default=0, blank=True, null=True) #kada naručiti
    zadnje_osvjezeno = models.DateField(verbose_name='Posljednje ažuriranje', auto_now=True, auto_now_add=False)
    export_to_CSV = models.BooleanField(default=False) #export u csv format

    def __str__(self):
        return self.naziv