
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.query import InstanceCheckMeta, QuerySet
from django.http import request
from . forms import AutomobilCreateForm, AutomobilUpdateForm, KilometriForm
from django.shortcuts import redirect, render
from django.core.paginator import Paginator



from . models import *



# Create your views here.
@login_required
def lista(request):
    queryset = Automobil.objects.all()
    context = {'queryset':queryset}
    return render(request, 'tasks/list.html', context)

@login_required
def dodaj(request):
    form = AutomobilCreateForm()

    if request.method == 'POST':
        form = AutomobilCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auti_app:lista')


    context = {'form': form}
    return render(request, 'tasks/dodaj.html', context)

@login_required
def uredi(request, pk):
	auto = Automobil.objects.get(id=pk)

	form = AutomobilUpdateForm(instance = auto)

	if request.method == 'POST':
		form = AutomobilUpdateForm(request.POST, instance=auto)
		if form.is_valid():

			form.save()
			return redirect('auti_app:lista')

	context = {'form':form}

	return render(request, 'tasks/uredi_automobil.html', context)

@login_required
def obrisi(request, pk):
    auto = Automobil.objects.get(id=pk)

    if request.method == 'POST':
        auto.delete()
        return redirect('auti_app:lista')

    context = {'auto':auto}
    return render(request,'tasks/obrisi.html', context)

@login_required
def detalji(request, pk):
    queryset = Automobil.objects.get(id=pk)
    context = {'queryset':queryset}
    return render(request, 'tasks/detalji.html', context)

@login_required
def kilometri(request, pk):
    queryset = Automobil.objects.get(id=pk)
    form = KilometriForm()
    pocetnaprikaz = queryset.zavrsna
    
    if request.method == 'POST':
        queryset.pocetna = queryset.zavrsna
        queryset.save()
        form = KilometriForm(request.POST, instance = queryset)
        if form.is_valid():
            instance = form.save(commit=False)
            if (instance.zavrsna <= instance.pocetna):
                messages.error(request, 'Završna kilometraža ne može biti manja od početne!')
                context = {'queryset':queryset,'form':form, 'pocetnaprikaz':pocetnaprikaz}
                return  render(request,'tasks/kilometri.html', context)

            else:
                instance.do_servisa = instance.servis_kilometri - instance.zavrsna
                instance.save()
                messages.success(request,'Uspješno ažurirano!')
            
            kilometri = Kilometraza.objects.create(
                ime = instance.ime,
                pocetna = instance.pocetna,
                zavrsna = instance.zavrsna,
                relacija = instance.relacija,
                dnevna_kilometraza = instance.zavrsna - instance.pocetna,
                zaduzio = str(request.user)
            )
            kilometri.save()
            return redirect('auti_app:detalji', pk)


    context = {'queryset':queryset, 'form':form, 'pocetnaprikaz':pocetnaprikaz}

    return render(request, 'tasks/kilometri.html', context)





@login_required
def kilometrilista(request, pk):
    queryset = Automobil.objects.get(id=pk)
    queryset1 = Kilometraza.objects.filter(ime = queryset.ime).order_by('-datum')

    paginator = Paginator(queryset1, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj, 'queryset':queryset}

    return render(request, 'tasks/kilometrilista.html', context)

