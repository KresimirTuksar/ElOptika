from django import forms
from django.core.exceptions import ValidationError
from . models import *

#

#

class SkladisteCreateForm(forms.ModelForm):
    
    class Meta:
        model = Skladiste
        fields = ['kategorija', 'naziv', 'kolicina']

    def clean_kategorija(self):
        kategorija = self.cleaned_data.get("kategorija")
        if not kategorija:
            raise forms.ValidationError('Ovo polje je obavezno')
        
        """ prevencija duplih unosa
        for instance  in Skladiste.objects.all():
            if instance.kategorija == kategorija:
                raise forms.ValidationError('Kategorija je več kreirana') """
        
        return kategorija
    
    def clean_naziv(self):
        kategorija = self.cleaned_data.get("naziv")
        if not kategorija:
            raise forms.ValidationError('Ovo polje je obavezno')
        return kategorija

class DodajKategorijuForm(forms.ModelForm):
    class Meta:
        model = Kategorija
        fields = ['ime']



class SkladisteSearchForm(forms.ModelForm):
    
    class Meta:
        model = Skladiste
        fields = ['naziv','kategorija','export_to_CSV']

class SkladisteUpdateForm(forms.ModelForm):

    class Meta:
        model = Skladiste
        fields = ['kategorija', 'naziv', 'kolicina']

class IzdavanjeForm(forms.ModelForm):
    class Meta:
        model = Skladiste
        fields = ['izdana_kolicina']

class ZaprimanjeForm(forms.ModelForm):
    class Meta:
        model = Skladiste
        fields = ['primljena_kolicina']

class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Skladiste
        fields = ['reorder_level']

""" class ZaduzivanjeForm(forms.ModelForm):

    class Meta:
        model = Skladiste
        fields = ['kolicina', 'zaduzio'] """