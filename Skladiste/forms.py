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


#Kablovi - BAKAR

class BakarCreateForm(forms.ModelForm):
    
    class Meta:
        model = KabelBakar
        fields = ['inv_broj','vlasnik','tip_kabela','proizvodjac', 'naziv','broj_pari','metraza']


    def clean(self):
        super(BakarCreateForm, self).clean()

      # dohvacanje vrijednosti u poljima
        inv_broj = self.cleaned_data.get('inv_broj')
        naziv = self.cleaned_data.get('naziv')
        vlasnik = self.cleaned_data.get("vlasnik")
        tip_kabela = self.cleaned_data.get("tip_kabela")
        broj_pari = self.cleaned_data.get('broj_pari')
        metraza = self.cleaned_data.get('metraza')
            
      # ovjera jesu li polja popunjena
        if not inv_broj :
            self._errors['inv_broj'] = self.error_class(['Ovo polje je obavezno'])
        
        if inv_broj < 1 :
            self._errors['inv_broj'] = self.error_class(['Inventurni broj mora biti pozitivan'])

        for instance  in KabelBakar.objects.all():
            if instance.inv_broj == inv_broj:
                self._errors['inv_broj'] = self.error_class(['Inventurni broj več postoji!'])


        if not naziv:
            self._errors['naziv'] = self.error_class(['Ovo polje je obavezno'])
        if not vlasnik:
            self._errors['vlasnik'] = self.error_class(['Ovo polje je obavezno'])
        if not tip_kabela:
            self._errors['tip_kabela'] = self.error_class(['Ovo polje je obavezno'])
        if not broj_pari:
            self._errors['broj_pari'] = self.error_class(['Ovo polje je obavezno'])
        if not metraza:
            self._errors['metraza'] = self.error_class(['Ovo polje je obavezno'])

        return self.cleaned_data



class BakarSearchForm(forms.ModelForm):
    class Meta:
        model = KabelBakar
        fields = ['naziv','inv_broj','tip_kabela','vlasnik','broj_pari','proizvodjac','export_to_CSV']

class BakarUpdateForm(forms.ModelForm):
    class Meta:
        model = KabelBakar
        fields = ['tip_kabela','proizvodjac', 'naziv','broj_pari','metraza',]

class BakarIzdajForm(forms.ModelForm):
    class Meta:
        model = KabelBakar
        fields = ['izdana_metraza', 'izdano_na','radnja']

    def clean(self):
            super(BakarIzdajForm, self).clean()

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


class BakarReorderLevelForm(forms.ModelForm):
    class Meta:
        model = KabelBakar
        fields = ['reorder_level']

class BakarHistorySearchForm(forms.ModelForm):
    class Meta:
        model = KabelBakarHistory
        fields = ['inv_broj','naziv','tip_kabela','proizvodjac','vlasnik','radnja','export_to_CSV'] #srediti pretragu zaduženja


#Kablovi - UTP

class UtpCreateForm(forms.ModelForm):
    
    class Meta:
        model = KabelUtp
        fields = ['inv_broj','vlasnik','tip_kabela','proizvodjac', 'naziv','metraza']


    def clean(self):
        super(UtpCreateForm, self).clean()

      # dohvacanje vrijednosti u poljima
        inv_broj = self.cleaned_data.get('inv_broj')
        naziv = self.cleaned_data.get('naziv')
        vlasnik = self.cleaned_data.get("vlasnik")
        tip_kabela = self.cleaned_data.get("tip_kabela")
        metraza = self.cleaned_data.get('metraza')
            
      # ovjera jesu li polja popunjena
        if not inv_broj :
            self._errors['inv_broj'] = self.error_class(['Ovo polje je obavezno'])
        
        if inv_broj < 1 :
            self._errors['inv_broj'] = self.error_class(['Inventurni broj mora biti pozitivan'])

        for instance  in KabelUtp.objects.all():
            if instance.inv_broj == inv_broj:
                self._errors['inv_broj'] = self.error_class(['Inventurni broj več postoji!'])


        if not naziv:
            self._errors['naziv'] = self.error_class(['Ovo polje je obavezno'])
        if not vlasnik:
            self._errors['vlasnik'] = self.error_class(['Ovo polje je obavezno'])
        if not tip_kabela:
            self._errors['tip_kabela'] = self.error_class(['Ovo polje je obavezno'])
        if not metraza:
            self._errors['metraza'] = self.error_class(['Ovo polje je obavezno'])
                
        return self.cleaned_data

        


class DodajTipForm(forms.ModelForm):
    class Meta:
        model = TipKabela
        fields = ['tip']

class UtpSearchForm(forms.ModelForm):
    class Meta:
        model = KabelUtp
        fields = ['naziv','inv_broj','tip_kabela','vlasnik','proizvodjac','export_to_CSV']

class UtpUpdateForm(forms.ModelForm):
    class Meta:
        model = KabelUtp
        fields = ['tip_kabela','proizvodjac', 'naziv','metraza',]

class UtpIzdajForm(forms.ModelForm):
    class Meta:
        model = KabelUtp
        fields = ['izdana_metraza', 'izdano_na','radnja']

    def clean(self):
            super(UtpIzdajForm, self).clean()

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


class UtpReorderLevelForm(forms.ModelForm):
    class Meta:
        model = KabelUtp
        fields = ['reorder_level']

class UtpHistorySearchForm(forms.ModelForm):
    class Meta:
        model = KabelUtpHistory
        fields = ['inv_broj','naziv','tip_kabela','proizvodjac','vlasnik','radnja','export_to_CSV'] #srediti pretragu zaduženja



#Cijevi

class CijevCreateForm(forms.ModelForm):
    
    class Meta:
        model = Cijev
        fields = ['inv_broj','vlasnik','vrsta_cijevi','proizvodjac', 'naziv','promjer','metraza']


    def clean(self):
        super(CijevCreateForm, self).clean()

      # dohvacanje vrijednosti u poljima
        inv_broj = self.cleaned_data.get('inv_broj')
        naziv = self.cleaned_data.get('naziv')
        vlasnik = self.cleaned_data.get("vlasnik")
        vrsta_cijevi = self.cleaned_data.get("vrsta_cijevi")
        promjer = self.cleaned_data.get("promjer")
        metraza = self.cleaned_data.get('metraza')
            
      # ovjera jesu li polja popunjena
        if not inv_broj :
            self._errors['inv_broj'] = self.error_class(['Ovo polje je obavezno'])
        
        if inv_broj < 1 :
            self._errors['inv_broj'] = self.error_class(['Inventurni broj mora biti pozitivan'])

        for instance  in KabelUtp.objects.all():
            if instance.inv_broj == inv_broj:
                self._errors['inv_broj'] = self.error_class(['Inventurni broj več postoji!'])


        if not naziv:
            self._errors['naziv'] = self.error_class(['Ovo polje je obavezno'])
        if not vlasnik:
            self._errors['vlasnik'] = self.error_class(['Ovo polje je obavezno'])
        if not vrsta_cijevi:
            self._errors['vrsta_cijevi'] = self.error_class(['Ovo polje je obavezno'])
        if not metraza:
            self._errors['metraza'] = self.error_class(['Ovo polje je obavezno'])
        if not promjer:
            self._errors['promjer'] = self.error_class(['Ovo polje je obavezno'])
                
        return self.cleaned_data

        

class DodajTipForm(forms.ModelForm):
    class Meta:
        model = TipKabela
        fields = ['tip']

class CijevSearchForm(forms.ModelForm):
    class Meta:
        model = Cijev
        fields = ['naziv','inv_broj','vrsta_cijevi','vlasnik','proizvodjac','promjer','export_to_CSV']

class CijevUpdateForm(forms.ModelForm):
    class Meta:
        model = Cijev
        fields = ['vrsta_cijevi','proizvodjac','promjer','naziv','metraza',]

class CijevIzdajForm(forms.ModelForm):
    class Meta:
        model = Cijev
        fields = ['izdana_metraza', 'izdano_na','radnja']

    def clean(self):
            super(CijevIzdajForm, self).clean()

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


class CijevReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Cijev
        fields = ['reorder_level']

class CijevHistorySearchForm(forms.ModelForm):
    class Meta:
        model = CijevHistory
        fields = ['inv_broj','naziv','vrsta_cijevi','proizvodjac','vlasnik','promjer','radnja','export_to_CSV'] #srediti pretragu zaduženja


#Materijal
class MaterijalCreateForm(forms.ModelForm):
    
    class Meta:
        model = Materijal
        fields = ['inv_broj','vlasnik','naziv','kolicina']


    def clean(self):
        super(MaterijalCreateForm, self).clean()

      # dohvacanje vrijednosti u poljima
        inv_broj = self.cleaned_data.get('inv_broj')
        naziv = self.cleaned_data.get('naziv')
        vlasnik = self.cleaned_data.get("vlasnik")
        kolicina = self.cleaned_data.get('kolicina')
            
      # ovjera jesu li polja popunjena
        if not inv_broj :
            self._errors['inv_broj'] = self.error_class(['Ovo polje je obavezno'])
        
        if inv_broj < 1 :
            self._errors['inv_broj'] = self.error_class(['Inventurni broj mora biti pozitivan'])

        for instance  in Materijal.objects.all():
            if instance.inv_broj == inv_broj:
                self._errors['inv_broj'] = self.error_class(['Inventurni broj več postoji!'])


        if not naziv:
            self._errors['naziv'] = self.error_class(['Ovo polje je obavezno'])
        if not vlasnik:
            self._errors['vlasnik'] = self.error_class(['Ovo polje je obavezno'])
        if not kolicina:
            self._errors['kolicina'] = self.error_class(['Ovo polje je obavezno'])

        return self.cleaned_data



class MaterijalSearchForm(forms.ModelForm):
    class Meta:
        model = Materijal
        fields = ['naziv','inv_broj','vlasnik','kolicina','export_to_CSV']

class MaterijalUpdateForm(forms.ModelForm):
    class Meta:
        model = Materijal
        fields = ['inv_broj','naziv','kolicina',]

class MaterijalIzdajForm(forms.ModelForm):
    class Meta:
        model = Materijal
        fields = ['izdana_kolicina', 'izdano_na','radnja']

    def clean(self):
            super(MaterijalIzdajForm, self).clean()

            izdana_kolicina = self.cleaned_data.get('izdana_kolicina')
            izdano_na = self.cleaned_data.get('izdano_na')
            radnja = self.cleaned_data.get("radnja")
            
            if not izdana_kolicina:
                self._errors['izdana_kolicina'] = self.error_class(['Ovo polje je obavezno'])
            if not izdano_na:
                self._errors['izdano_na'] = self.error_class(['Ovo polje je obavezno'])
            if not radnja:
                self._errors['radnja'] = self.error_class(['Ovo polje je obavezno'])

            return self.cleaned_data


class MaterijalReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Materijal
        fields = ['reorder_level']

class MaterijalHistorySearchForm(forms.ModelForm):
    class Meta:
        model = MaterijalHistory
        fields = ['inv_broj','naziv','vlasnik','radnja','export_to_CSV'] #srediti pretragu zaduženja


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