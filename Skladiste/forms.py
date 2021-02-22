from django import forms
from django.core.exceptions import ValidationError
from . models import *

#

#Kablovi - OPTIKA

class OptikaCreateForm(forms.ModelForm):
    
    class Meta:
        model = KabelOptika
        fields = ['inv_broj','vlasnik','tip_kabela','proizvodjac', 'naziv','broj_niti','metraza']


    def clean(self):
        super(OptikaCreateForm, self).clean()

      # dohvacanje vrijednosti u poljima
        inv_broj = self.cleaned_data.get('inv_broj')
        naziv = self.cleaned_data.get('naziv')
        vlasnik = self.cleaned_data.get("vlasnik")
        tip_kabela = self.cleaned_data.get("tip_kabela")
        broj_niti = self.cleaned_data.get('broj_niti')
        metraza = self.cleaned_data.get('metraza')
            
      # ovjera jesu li polja popunjena
        if not inv_broj :
            self._errors['inv_broj'] = self.error_class(['Ovo polje je obavezno'])
        
        if inv_broj < 1 :
            self._errors['inv_broj'] = self.error_class(['Inventurni broj mora biti pozitivan'])

        for instance  in KabelOptika.objects.all():
            if instance.inv_broj == inv_broj:
                self._errors['inv_broj'] = self.error_class(['Inventurni broj več postoji!'])


        if not naziv:
            self._errors['naziv'] = self.error_class(['Ovo polje je obavezno'])
        if not vlasnik:
            self._errors['vlasnik'] = self.error_class(['Ovo polje je obavezno'])
        if not tip_kabela:
            self._errors['tip_kabela'] = self.error_class(['Ovo polje je obavezno'])
        if not broj_niti:
            self._errors['broj_niti'] = self.error_class(['Ovo polje je obavezno'])
        if not metraza:
            self._errors['metraza'] = self.error_class(['Ovo polje je obavezno'])
                
        
        for instance  in KabelOptika.objects.all():
            if instance.inv_broj == inv_broj:
                self._errors['inv_broj'] = self.error_class(['Inventurni broj več postoji!'])

        return self.cleaned_data

        


class DodajTipForm(forms.ModelForm):
    class Meta:
        model = TipKabela
        fields = ['tip']

class OptikaSearchForm(forms.ModelForm):
    class Meta:
        model = KabelOptika
        fields = ['naziv','inv_broj','tip_kabela','vlasnik','broj_niti','proizvodjac','export_to_CSV']

class OptikaUpdateForm(forms.ModelForm):
    class Meta:
        model = KabelOptika
        fields = ['tip_kabela','proizvodjac', 'naziv','broj_niti','metraza',]

class OptikaIzdajForm(forms.ModelForm):
    class Meta:
        model = KabelOptika
        fields = ['izdana_metraza', 'izdano_na','radnja']

    def clean(self):
            super(OptikaIzdajForm, self).clean()

            izdana_metraza = self.cleaned_data.get('izdana_metraza')
            izdano_na = self.cleaned_data.get('izdano_na')
            radnja = self.cleaned_data.get("radnja")
            
            if not izdana_metraza:
                self._errors['izdana_metraza'] = self.error_class(['Ovo polje je obavezno'])
            if not izdano_na:
                self._errors['izdano_na'] = self.error_class(['Ovo polje je obavezno'])
            if not radnja:
                self._errors['radnja'] = self.error_class(['Ovo polje je obavezno'])

            return self.cleaned_data


class OptikaReorderLevelForm(forms.ModelForm):
    class Meta:
        model = KabelOptika
        fields = ['reorder_level']

class OptikaHistorySearchForm(forms.ModelForm):
    class Meta:
        model = KabelOptikaHistory
        fields = ['inv_broj','naziv','tip_kabela','proizvodjac','vlasnik','radnja','export_to_CSV'] #srediti pretragu zaduženja


#########
class SkladisteCreateForm(forms.ModelForm):
    
    class Meta:
        model = Skladiste
        fields = ['naziv','kolicina','kategorija']

    """ def clean_kategorija(self):
        kategorija = self.cleaned_data.get("kategorija")
        if not kategorija:
            raise forms.ValidationError('Ovo polje je obavezno')
        
        #prevencija duplih unosa
        for instance  in Skladiste.objects.all():
            if instance.kategorija == kategorija:
                raise forms.ValidationError('Kategorija je več kreirana')
        
        return tip
    
    def clean_naziv(self):
        kategorija = self.cleaned_data.get("naziv")
        if not kategorija:
            raise forms.ValidationError('Ovo polje je obavezno')
        return kategorija """

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

class ZaduzivanjeForm(forms.ModelForm):

    class Meta:
        model = Skladiste
        fields = ['zaduzena_kolicina', 'zaduzio']