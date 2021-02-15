from . forms import DodajKategorijuForm, IzdavanjeForm, ReorderLevelForm, SkladisteCreateForm, SkladisteSearchForm, SkladisteUpdateForm, ZaprimanjeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *


from django.http import HttpResponse, request, response
import csv
# Create your views here.
@login_required
def skladiste(request):
    form = SkladisteSearchForm(request.POST)
    queryset = Skladiste.objects.all()
    context = {'queryset':queryset, 'form':form}

    if request.method == 'POST':
        queryset = Skladiste.objects.filter(naziv__icontains=form['naziv'].value(),
                                           # kategorija__icontains=form['kategorija'].value()
        )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['KATEGORIJA', 'NAZIV', 'KOLIČINA'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.kategorija, stock.naziv, stock.kolicina])

            return response
        else:
                
            context = {'form':form, 'queryset':queryset}

    return render(request,'skladiste.html', context )

    
@login_required
def dodaj(request):
    form = SkladisteCreateForm()

    if request.method =='POST':
        form = SkladisteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Uspješno dodano!')
            return redirect('skladiste_app:skladiste')

    context = {'form': form,}
    return render(request, 'dodaj.html', context)

@login_required
def dodaj_kategoriju(request):
    form = DodajKategorijuForm()
    if request.method == 'POST':
        form = DodajKategorijuForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Kategorija dodana!')
            return redirect('skladiste_app:skladiste')

    context = {'form':form}
    return render(request, 'dodaj_kategoriju.html', context)


@login_required
def uredi(request, pk):
	queryset = Skladiste.objects.get(id=pk)

	form = SkladisteUpdateForm(instance = queryset)

	if request.method == 'POST':
		form = SkladisteUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('skladiste_app:skladiste')

	context = {'form':form}

	return render(request, 'uredi_artikl.html', context)

@login_required
def obrisi_artikl(request, pk):
    queryset = Skladiste.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('skladiste_app:skladiste')
    return render(request, 'obrisi_artikl.html')

@login_required
def detalji(request, pk):
    queryset = Skladiste.objects.get(id=pk)
    context = {'queryset' : queryset}
    
    return render(request, 'artikl_detalji.html', context)

@login_required
def izdavanje(request, pk):
    queryset = Skladiste.objects.get(id=pk)
    form = IzdavanjeForm(request.POST, instance=queryset)

    if request.method =='POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.kolicina -= instance.izdana_kolicina
            instance.izdao = str(request.user)
            instance.save()
            izdavanje_history = SkladisteHistory(
                id = instance.id,
                zadnje_osvjezeno = instance.zadnje_osvjezeno,
                kategorija_id = instance.kategorija_id,
                naziv = instance.naziv,
                kolicina = instance.kolicina,
                izdano_na = instance.izdano_na,
                izdao = instance.izdao,
                izdana_kolicina = instance.izdana_kolicina,
            )
            izdavanje_history.save()

            messages.success(request, 'Uspješno izdano. Još ' + str(instance.kolicina) + ' ' + str(instance.naziv) + ' ostalo na skladištu.')
            return redirect('skladiste_app:skladiste')

    context = {'queryset':queryset,
                'form':form,
                'username': 'Izdao: '+str(request.user)
    }

    return  render(request, 'izdavanje.html', context)

@login_required
def zaprimanje(request, pk):
    queryset = Skladiste.objects.get(id=pk)
    form = ZaprimanjeForm(request.POST, instance=queryset)

    if request.method =='POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.kolicina += instance.primljena_kolicina
            instance.zaprimio = str(request.user)
            instance.save()
            messages.success(request, 'Artikl zaprimljen. Trenutno je ' + str(instance.kolicina) + ' ' + str(instance.naziv) + ' na skladištu.')
            izdavanje_history = SkladisteHistory(
                id = instance.id,
                zadnje_osvjezeno = instance.zadnje_osvjezeno,
                kategorija_id = instance.kategorija_id,
                naziv = instance.naziv,
                kolicina = instance.kolicina,
                primljena_kolicina = instance.primljena_kolicina,
                zaprimio = instance.zaprimio,
            )
            izdavanje_history.save()
            return redirect('skladiste_app:skladiste')

    context = {'queryset':queryset,
                'form':form,
                'username': 'Izdao: '+str(request.user)
    }


    return  render(request, 'izdavanje.html', context)

""" def zaduzivanje(request, pk):
    queryset = Skladiste.objects.get(id=pk)
    form = ZaduzivanjeForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            
            form.save()

            return redirect('skladiste_app:skladiste')

    context = {'form': form}
    return render(request, 'zaduzivanje.html', context) """

@login_required
def reorder_level(request, pk):
    queryset = Skladiste.objects.get(id=pk)
    form = ReorderLevelForm(request.POST or None, instance = queryset)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Nivo naručivanja za ' + str(instance.naziv) + ' postavljen je na ' + str(instance.reorder_level) + '.')

            return redirect('skladiste_app:skladiste')

    context = {'instance': queryset, 'form': form}
    return render (request, 'reorder_level.html', context)

@login_required
def skladiste_history(request):
    queryset = SkladisteHistory.objects.all()
    context = {'queryset':queryset}

    return render(request, 'skladiste_history.html', context)