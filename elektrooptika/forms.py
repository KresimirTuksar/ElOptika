from django import forms

# Email form
class Kontakt(forms.Form):
    ime = forms.CharField(max_length=50, required=True)
    prezime = forms.CharField(max_length=50, required=True)
    adresa = forms.EmailField(max_length=150, required=True)
    poruka = forms.CharField(widget=forms.Textarea, max_length=2000, required=True)