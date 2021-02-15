
from django.contrib.auth.decorators import login_required
from django.http import request
from . forms import AutomobilForm, UserLoginForm
from django.shortcuts import redirect, render


from . models import *



# Create your views here.
@login_required
def lista(request):
    auti = Automobil.objects.all

    context = {'auti': auti}
    return render(request, 'tasks/list.html', context)

@login_required
def dodaj(request):
    form = AutomobilForm()

    if request.method == 'POST':
        form = AutomobilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auti_app:lista')

    context = {'form': form}
    return render(request, 'tasks/dodaj.html', context)

@login_required
def uredi(request, pk):
	auto = Automobil.objects.get(id=pk)

	form = AutomobilForm(instance = auto)

	if request.method == 'POST':
		form = AutomobilForm(request.POST, instance=auto)
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