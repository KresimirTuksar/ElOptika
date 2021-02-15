from elektrooptika.forms import Kontakt
from django.shortcuts import redirect, render
from . forms import Kontakt
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse
# Create your views here.
def index(request):
    
    return render(request, 'pocetna.html')

def reference(request):
    
    return render(request, 'reference.html')

def kontakt(request):
    if request.method == 'POST':
        form = Kontakt(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = { 
                'ime':form.cleaned_data['ime'],
                'prezime':form.cleaned_data['prezime'],
                'adresa':form.cleaned_data['adresa'],
                'poruka':form.cleaned_data['poruka'],
            }
            poruka = "\n".join(body.values())

            try:
                send_mail(subject, poruka, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('invalid header found')
            return redirect('elektro:home')
    form = Kontakt()
    return render(request, 'kontakt.html', {'form': form})