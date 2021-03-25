from auti_app.models import Automobil, Kilometraza
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class AutomobilCreateForm(forms.ModelForm):
    

    class Meta:
        model = Automobil
        fields = ['ime','marka','tablica','zavrsna','registracija_datum','servis_datum','servis_kilometri','atest']
        widgets = {
            'atest': forms.NumberInput(attrs={'type': 'date'}),
            'registracija_datum': forms.NumberInput(attrs={'type': 'date'}),
            'servis_datum': forms.NumberInput(attrs={'type': 'date'}),
            }

    def clean(self):
        super(AutomobilCreateForm, self).clean()

      # dohvacanje vrijednosti u poljima
        ime = self.cleaned_data.get('ime')
        marka = self.cleaned_data.get('marka')
        tablica = self.cleaned_data.get("tablica")
        zavrsna = self.cleaned_data.get("zavrsna")
        registracija_datum = self.cleaned_data.get('registracija_datum')
        servis_datum = self.cleaned_data.get('servis_datum')
        

        if not ime :
            self._errors['ime'] = self.error_class(['Ovo polje je obavezno'])
        if not marka:
            self._errors['marka'] = self.error_class(['Ovo polje je obavezno'])
        if not tablica:
            self._errors['tablica'] = self.error_class(['Ovo polje je obavezno'])
        for instance  in Automobil.objects.all():
            if instance.tablica == tablica:
                self._errors['tablica'] = self.error_class(['Registarska oznaka več postoji!'])
        if not zavrsna:
            self._errors['zavrsna'] = self.error_class(['Ovo polje je obavezno'])
        if not registracija_datum:
            self._errors['registracija_datum'] = self.error_class(['Ovo polje je obavezno'])
        if not servis_datum:
            self._errors['servis_datum'] = self.error_class(['Ovo polje je obavezno'])

        return self.cleaned_data

class AutomobilUpdateForm(forms.ModelForm):

    class Meta:
        model = Automobil
        fields = ['ime','marka','tablica','pocetna','registracija_datum','servis_datum','servis_kilometri','atest']
        widgets = {
            'atest': forms.NumberInput(attrs={'type': 'date'}),
            'registracija_datum': forms.NumberInput(attrs={'type': 'date'}),
            'servis_datum': forms.NumberInput(attrs={'type': 'date'}),
            }
    def clean(self):
        super(AutomobilUpdateForm, self).clean()

      # dohvacanje vrijednosti u poljima
        ime = self.cleaned_data.get('ime')
        marka = self.cleaned_data.get('marka')
        tablica = self.cleaned_data.get("tablica")
        pocetna = self.cleaned_data.get("pocetna")
        registracija_datum = self.cleaned_data.get('registracija_datum')
        servis_datum = self.cleaned_data.get('servis_datum')
        

        if not ime :
            self._errors['ime'] = self.error_class(['Ovo polje je obavezno'])
        if not marka:
            self._errors['marka'] = self.error_class(['Ovo polje je obavezno'])
        if not tablica:
            self._errors['tablica'] = self.error_class(['Ovo polje je obavezno'])
        if not pocetna:
            self._errors['pocetna'] = self.error_class(['Ovo polje je obavezno'])
        if not registracija_datum:
            self._errors['registracija_datum'] = self.error_class(['Ovo polje je obavezno'])
        if not servis_datum:
            self._errors['servis_datum'] = self.error_class(['Ovo polje je obavezno'])

        return self.cleaned_data

class KilometriForm(forms.ModelForm):
    class Meta:
        model = Automobil
        fields = ['zavrsna','relacija']

    def clean(self):
        super(KilometriForm, self).clean()

      # dohvacanje vrijednosti u poljima
        zavrsna = self.cleaned_data.get('zavrsna')
        relacija = self.cleaned_data.get('relacija')
        
        if not zavrsna :
            self._errors['zavrsna'] = self.error_class(['Ovo polje je obavezno'])
        if not relacija:
            self._errors['relacija'] = self.error_class(['Ovo polje je obavezno'])
        
        return self.cleaned_data


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    