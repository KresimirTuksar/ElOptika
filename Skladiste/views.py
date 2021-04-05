from . forms import ALatCreateForm, AlatSearchForm, AlatUpdateForm, AlatZaduziForm, BakarCreateForm, BakarHistorySearchForm, BakarIzdajForm, BakarReorderLevelForm, BakarSearchForm, BakarUpdateForm, CijevCreateForm, CijevHistorySearchForm, CijevIzdajForm, CijevReorderLevelForm, CijevSearchForm, CijevUpdateForm, DodajKategorijuForm, DodajTipForm, IzdavanjeForm, MaterijalCreateForm, MaterijalIzdajForm, MaterijalReorderLevelForm, MaterijalSearchForm, MaterijalUpdateForm, OptikaCreateForm, OptikaHistorySearchForm, OptikaIzdajForm, OptikaReorderLevelForm, OptikaSearchForm, OptikaUpdateForm, ReorderLevelForm, SkladisteCreateForm, SkladisteSearchForm, SkladisteUpdateForm, UtpCreateForm, UtpHistorySearchForm, UtpIzdajForm, UtpReorderLevelForm, UtpSearchForm, UtpUpdateForm, ZaprimanjeForm, ZaduzivanjeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
import datetime
from . models import *


from django.http import HttpResponse, request, response
import csv
# Create your views here.

#dodaj tip kabela
@login_required
def dodaj_tip(request):
    form = DodajTipForm()
    if request.method == 'POST':
        form = DodajTipForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Tip kabela dodan!')
            return redirect('skladiste_app:skladiste')

    context = {'form':form}
    return render(request, 'forma.html', context)



#kablovi - OPTIKA

@login_required
def listoptika(request):
    form = OptikaSearchForm(request.POST)
    queryset = KabelOptika.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        #tip_kabela = (form['tip_kabela'].value)
        queryset = KabelOptika.objects.filter(naziv__icontains = form['naziv'].value(),
                                            inv_broj__icontains = form['inv_broj'].value(),
                                            tip_kabela__tip__icontains =form['tip_kabela'].value(),
                                            vlasnik__icontains = form['vlasnik'].value(),
                                            broj_niti__icontains = form['broj_niti'].value(),
                                            proizvodjac__icontains = form['proizvodjac'].value()
        
        )
        #if (tip_kabela != ''):
            #queryset = queryset.filter(tip_kabela_id = tip_kabela)

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['NAZIV', 'INVENTURNI BROJ', 'TIP KABELA', 'VLASNIK','BROJ NITI','PROIZVOĐAČ'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.naziv, stock.inv_broj, stock.tip_kabela, stock.vlasnik, stock.broj_niti, stock.proizvodjac])

            return response
        else:

            context = {'form':form, 'queryset':queryset}
    
    return render(request,'skladisteoptika.html', context )


@login_required
def optika_dodaj(request):
    queryset = KabelOptika.objects.all()
    form = OptikaCreateForm()

    if request.method =='POST':
        form = OptikaCreateForm(request.POST)
        if form.is_valid():
            novo = form.save(commit=False)
            novo.kreirao = request.user
            novo.save()
            messages.success(request, 'Uspješno dodano!')
            return redirect('skladiste_app:listoptika')

    context = {'form': form, 'queryset':queryset}
    return render(request, 'forma.html', context)




@login_required
def optika_detalji(request, pk):
    queryset = KabelOptika.objects.get(id=pk)
    context = {'queryset':queryset,}
    
    return render(request, 'optika_detalji.html', context)

@login_required
def optika_uredi(request, pk):
	queryset = KabelOptika.objects.get(id=pk)

	form = OptikaUpdateForm(instance = queryset)

	if request.method == 'POST':
		form = OptikaUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('skladiste_app:optika_detalji', pk)

	context = {'form':form}

	return render(request, 'uredi_artikl.html', context)


@login_required
def optika_izdaj(request, pk):
    queryset = KabelOptika.objects.get(id=pk)
    
    form = OptikaIzdajForm()

    if request.method =='POST':
        form = OptikaIzdajForm(request.POST, instance=queryset)
        if form.is_valid():
            
            instance = form.save(commit=False)
            instance.metraza -= instance.izdana_metraza
            instance.izdao = str(request.user)
            if (instance.metraza >=0):
                messages.success(request, 'Uspješno izdano. Još ' + str(instance.metraza) + 'metara ostalo na skladištu.')
                instance.save()
            else:
                messages.error(request,'Nedovoljno kabela. Trenutno dostupno ' + str(queryset.metraza) + ' metara.')
                context = {'queryset':queryset,'form':form}
                return  render(request, 'izdavanje.html', context)
            # kopiranje odabranog objekta u history
            history = KabelOptikaHistory.objects.create(
                #id = instance.id,
                inv_broj = instance.inv_broj,
                naziv = instance.naziv,
                proizvodjac = instance.proizvodjac,
                vlasnik = instance.vlasnik,
                tip_kabela = instance.tip_kabela,
                broj_niti = instance.broj_niti,
                metraza = instance.metraza,
                izdana_metraza = instance.izdana_metraza,
                izdano_na = instance.izdano_na,
                izdao = instance.izdao,
                radnja = instance.radnja,
                zadnje_osvjezeno = instance.zadnje_osvjezeno,
            )
            history.save()

            return redirect('skladiste_app:optika_detalji', pk)

    context = {'queryset':queryset,
            
                'form':form,
                'username': 'Izdao: '+str(request.user)
    }

    return  render(request, 'izdavanje.html', context)


@login_required
def optika_obrisi(request, pk):
    queryset = KabelOptika.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('skladiste_app:listoptika')
    return render(request, 'forma.html')

@login_required
def optika_reorder_level(request, pk):
    queryset = KabelOptika.objects.get(id=pk)
    form = OptikaReorderLevelForm(request.POST or None, instance = queryset)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Nivo naručivanja za ' + str(instance.naziv) + ' postavljen je na ' + str(instance.reorder_level) + '.')

            return redirect('skladiste_app:optika_detalji', pk)

    context = {'instance': queryset, 'form': form}
    return render (request, 'reorder_level.html', context)

@login_required
def optika_history(request):
    form = OptikaHistorySearchForm(request.POST)
    queryset = KabelOptikaHistory.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        queryset = KabelOptikaHistory.objects.filter(naziv__icontains = form['naziv'].value(),
                                            inv_broj__icontains = form['inv_broj'].value(),
                                            proizvodjac__icontains = form['proizvodjac'].value(),
                                            #tip_kabela__icontains = form['tip_kabela'].value(),
                                            vlasnik__icontains = form['vlasnik'].value(),
                                            #izdano_na__icontains = form['izdano_na'].value(),
                                            radnja__icontains = form['radnja'].value()
        )
        
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['NAZIV', 'INVENTURNI BROJ', 'TIP KABELA', 'VLASNIK','BROJ NITI','PROIZVOĐAČ'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.naziv, stock.inv_broj, stock.tip_kabela, stock.vlasnik, stock.broj_niti, stock.proizvodjac])

            return response
        else:

            context = {'form':form, 'queryset':queryset}

    return render(request, 'optikahistory.html', context)
###############
#kablovi - BAKAR

@login_required
def listbakar(request):
    form = BakarSearchForm(request.POST)
    queryset = KabelBakar.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        #tip_kabela = (form['tip_kabela'].value)
        queryset = KabelBakar.objects.filter(naziv__icontains = form['naziv'].value(),
                                            inv_broj__icontains = form['inv_broj'].value(),
                                            #tip_kabela__tip__contains = form['tip_kabela'].value(),
                                            vlasnik__icontains = form['vlasnik'].value(),
                                            broj_pari__icontains = form['broj_pari'].value(),
                                            proizvodjac__icontains = form['proizvodjac'].value()
        
        )
        #if (tip_kabela != ''):
        #    queryset = queryset.filter(tip_kabela_id = tip_kabela)

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['NAZIV', 'INVENTURNI BROJ', 'TIP KABELA', 'VLASNIK','BROJ PARI','PROIZVOĐAČ'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.naziv, stock.inv_broj, stock.tip_kabela, stock.vlasnik, stock.broj_pari, stock.proizvodjac])

            return response
        else:

            context = {'form':form, 'queryset':queryset}
    
    return render(request,'skladistebakar.html', context )


@login_required
def bakar_dodaj(request):
    queryset = KabelBakar.objects.all()
    form = BakarCreateForm()

    if request.method =='POST':
        form = BakarCreateForm(request.POST)
        if form.is_valid():
            kreirao = str(request.user)
            form.save()
            messages.success(request, 'Uspješno dodano!')
            return redirect('skladiste_app:listbakar')

    context = {'form': form, 'queryset':queryset}
    return render(request, 'forma.html', context)




@login_required
def bakar_detalji(request, pk):
    queryset = KabelBakar.objects.get(id=pk)
    context = {'queryset':queryset}
    
    return render(request, 'bakar_detalji.html', context)

@login_required
def bakar_uredi(request, pk):
	queryset = KabelBakar.objects.get(id=pk)

	form = BakarUpdateForm(instance = queryset)

	if request.method == 'POST':
		form = BakarUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('skladiste_app:bakar_detalji', pk)

	context = {'form':form}

	return render(request, 'forma.html', context)


@login_required
def bakar_izdaj(request, pk):
    queryset = KabelBakar.objects.get(id=pk)
    form = BakarIzdajForm()

    if request.method =='POST':
        form = BakarIzdajForm(request.POST, instance=queryset)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.metraza -= instance.izdana_metraza
            instance.izdao = str(request.user)
            if (instance.metraza >=0):
                messages.success(request, 'Uspješno izdano. Još ' + str(instance.metraza) + ' metara ostalo na skladištu.')
                instance.save()
            else:
                messages.error(request,'Nedovoljno kabela')
                context = {'queryset':queryset,'form':form}
                return  render(request, 'forma.html', context)
            # kopiranje odabranog objekta u history
            history = KabelBakarHistory.objects.create(
                #id = instance.id,
                inv_broj = instance.inv_broj,
                naziv = instance.naziv,
                proizvodjac = instance.proizvodjac,
                vlasnik = instance.vlasnik,
                tip_kabela = instance.tip_kabela,
                broj_pari = instance.broj_pari,
                metraza = instance.metraza,
                izdana_metraza = instance.izdana_metraza,
                izdano_na = instance.izdano_na,
                izdao = instance.izdao,
                radnja = instance.radnja,
                zadnje_osvjezeno = instance.zadnje_osvjezeno,
            )
            history.save()

            return redirect('skladiste_app:bakar_detalji', pk)

    context = {'queryset':queryset,
                'form':form,
                'username': 'Izdao: '+str(request.user)
    }

    return  render(request, 'forma.html', context)


@login_required
def bakar_obrisi(request, pk):
    queryset = KabelBakar.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('skladiste_app:listbakar')
    return render(request, 'obrisi_artikl.html')

@login_required
def bakar_reorder_level(request, pk):
    queryset = KabelBakar.objects.get(id=pk)
    form = BakarReorderLevelForm(request.POST or None, instance = queryset)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Nivo naručivanja za ' + str(instance.naziv) + ' postavljen je na ' + str(instance.reorder_level) + '.')

            return redirect('skladiste_app:bakar_detalji', pk)

    context = {'instance': queryset, 'form': form}
    return render (request, 'forma.html', context)

@login_required
def bakar_history(request):
    form = BakarHistorySearchForm(request.POST)
    queryset = KabelBakarHistory.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        queryset = KabelBakarHistory.objects.filter(naziv__icontains = form['naziv'].value(),
                                            inv_broj__icontains = form['inv_broj'].value(),
                                            proizvodjac__icontains = form['proizvodjac'].value(),
                                            #tip_kabela__icontains = form['tip_kabela'].value(),
                                            vlasnik__icontains = form['vlasnik'].value(),
                                            #izdano_na__icontains = form['izdano_na'].value(),
                                            radnja__icontains = form['radnja'].value()
        )
        
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['NAZIV', 'INVENTURNI BROJ', 'TIP KABELA', 'VLASNIK','BROJ PARICA','PROIZVOĐAČ'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.naziv, stock.inv_broj, stock.tip_kabela, stock.vlasnik, stock.broj_pari, stock.proizvodjac])

            return response
        else:

            context = {'form':form, 'queryset':queryset}

    return render(request, 'bakarhistory.html', context)
###########################


#kablovi - UTP

@login_required
def listutp(request):
    form = UtpSearchForm(request.POST)
    queryset = KabelUtp.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        #tip_kabela = (form['tip_kabela'].value)
        queryset = KabelUtp.objects.filter(naziv__icontains = form['naziv'].value(),
                                            inv_broj__icontains = form['inv_broj'].value(),
                                            #tip_kabela__tip__contains = form['tip_kabela'].value(),
                                            vlasnik__icontains = form['vlasnik'].value(),
                                            proizvodjac__icontains = form['proizvodjac'].value()
        
        )
        #if (tip_kabela != ''):
        #    queryset = queryset.filter(tip_kabela_id = tip_kabela)

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['NAZIV', 'INVENTURNI BROJ', 'TIP KABELA', 'VLASNIK','BROJ NITI','PROIZVOĐAČ'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.naziv, stock.inv_broj, stock.tip_kabela, stock.vlasnik, stock.broj_niti, stock.proizvodjac])

            return response
        else:

            context = {'form':form, 'queryset':queryset}
    
    return render(request,'skladisteutp.html', context )


@login_required
def utp_dodaj(request):
    queryset = KabelUtp.objects.all()
    form = UtpCreateForm()

    if request.method =='POST':
        form = UtpCreateForm(request.POST)
        if form.is_valid():
            kreirao = str(request.user)
            form.save()
            messages.success(request, 'Uspješno dodano!')
            return redirect('skladiste_app:listutp')

    context = {'form': form, 'queryset':queryset}
    return render(request, 'forma.html', context)



@login_required
def utp_detalji(request, pk):
    queryset = KabelUtp.objects.get(id=pk)
    context = {'queryset':queryset}
    
    return render(request, 'utp_detalji.html', context)

@login_required
def utp_uredi(request, pk):
	queryset = KabelUtp.objects.get(id=pk)

	form = UtpUpdateForm(instance = queryset)

	if request.method == 'POST':
		form = UtpUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('skladiste_app:utp_detalji', pk)

	context = {'form':form}

	return render(request, 'forma.html', context)


@login_required
def utp_izdaj(request, pk):
    queryset = KabelUtp.objects.get(id=pk)
    form = UtpIzdajForm()

    if request.method =='POST':
        form = UtpIzdajForm(request.POST, instance=queryset)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.metraza -= instance.izdana_metraza
            instance.izdao = str(request.user)
            if (instance.metraza >=0):
                messages.success(request, 'Uspješno izdano. Još ' + str(instance.metraza) + ' metara ostalo na skladištu.')
                instance.save()
            else:
                messages.error(request,'Nedovoljno kabela')
                context = {'queryset':queryset,'form':form}
                return  render(request, 'forma.html', context)
            # kopiranje odabranog objekta u history
            history = KabelUtpHistory.objects.create(
                #id = instance.id,
                inv_broj = instance.inv_broj,
                naziv = instance.naziv,
                proizvodjac = instance.proizvodjac,
                vlasnik = instance.vlasnik,
                tip_kabela = instance.tip_kabela,
                metraza = instance.metraza,
                izdana_metraza = instance.izdana_metraza,
                izdano_na = instance.izdano_na,
                izdao = instance.izdao,
                radnja = instance.radnja,
                zadnje_osvjezeno = instance.zadnje_osvjezeno,
            )
            history.save()

            return redirect('skladiste_app:utp_detalji', pk)

    context = {'queryset':queryset,
                'form':form,
                'username': 'Izdao: '+str(request.user)
    }

    return  render(request, 'forma.html', context)


@login_required
def utp_obrisi(request, pk):
    queryset = get_object_or_404(KabelUtp,id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('skladiste_app:listutp')
    return render(request, 'obrisi_artikl.html')

@login_required
def utp_reorder_level(request, pk):
    queryset = KabelUtp.objects.get(id=pk)
    form = UtpReorderLevelForm(request.POST or None, instance = queryset)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Nivo naručivanja za ' + str(instance.naziv) + ' postavljen je na ' + str(instance.reorder_level) + '.')

            return redirect('skladiste_app:utp_detalji', pk)

    context = {'instance': queryset, 'form': form}
    return render (request, 'forma.html', context)

@login_required
def utp_history(request):
    form = UtpHistorySearchForm(request.POST)
    queryset = KabelUtpHistory.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        queryset = KabelUtpHistory.objects.filter(naziv__icontains = form['naziv'].value(),
                                            inv_broj__icontains = form['inv_broj'].value(),
                                            proizvodjac__icontains = form['proizvodjac'].value(),
                                            #tip_kabela__icontains = form['tip_kabela'].value(),
                                            vlasnik__icontains = form['vlasnik'].value(),
                                            #izdano_na__icontains = form['izdano_na'].value(),
                                            radnja__icontains = form['radnja'].value()
        )
        
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['NAZIV', 'INVENTURNI BROJ', 'TIP KABELA', 'VLASNIK','BROJ NITI','PROIZVOĐAČ'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.naziv, stock.inv_broj, stock.tip_kabela, stock.vlasnik, stock.broj_niti, stock.proizvodjac])

            return response
        else:

            context = {'form':form, 'queryset':queryset}

    return render(request, 'utphistory.html', context)

#################################
#kablovi - BAKAR

@login_required
def listcijev(request):
    form = CijevSearchForm(request.POST)
    queryset = Cijev.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        #tip_kabela = (form['tip_kabela'].value)
        queryset = Cijev.objects.filter(naziv__icontains = form['naziv'].value(),
                                            inv_broj__icontains = form['inv_broj'].value(),
                                            #tip_kabela__tip__contains = form['tip_kabela'].value(),
                                            vlasnik__icontains = form['vlasnik'].value(),
                                            promjer__icontains = form['promjer'].value(),
                                            proizvodjac__icontains = form['proizvodjac'].value()
        
        )
        #if (tip_kabela != ''):
        #    queryset = queryset.filter(tip_kabela_id = tip_kabela)

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['NAZIV', 'INVENTURNI BROJ', 'Vrsta CIJEVI', 'VLASNIK','PPROMJER','PROIZVOĐAČ'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.naziv, stock.inv_broj, stock.vrsta_cijevi, stock.vlasnik, stock.promjer, stock.proizvodjac])

            return response
        else:

            context = {'form':form, 'queryset':queryset}
    
    return render(request,'skladistecijevi.html', context )


@login_required
def cijev_dodaj(request):
    queryset = Cijev.objects.all()
    form = CijevCreateForm()

    if request.method =='POST':
        form = CijevCreateForm(request.POST)
        if form.is_valid():
            kreirao = str(request.user)
            form.save()
            messages.success(request, 'Uspješno dodano!')
            return redirect('skladiste_app:listcijevi')

    context = {'form': form, 'queryset':queryset}
    return render(request, 'forma.html', context)





@login_required
def cijev_detalji(request, pk):
    queryset = Cijev.objects.get(id=pk)
    context = {'queryset':queryset}
    
    return render(request, 'cijevi_detalji.html', context)

@login_required
def cijev_uredi(request, pk):
	queryset = Cijev.objects.get(id=pk)

	form = CijevUpdateForm(instance = queryset)

	if request.method == 'POST':
		form = CijevUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('skladiste_app:cijevi_detalji', pk)

	context = {'form':form}

	return render(request, 'forma.html', context)


@login_required
def cijev_izdaj(request, pk):
    queryset = Cijev.objects.get(id=pk)
    form = CijevIzdajForm()

    if request.method =='POST':
        form = CijevIzdajForm(request.POST, instance=queryset)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.metraza -= instance.izdana_metraza
            instance.izdao = str(request.user)
            if (instance.metraza >=0):
                messages.success(request, 'Uspješno izdano. Još ' + str(instance.metraza) + ' metara ostalo na skladištu.')
                instance.save()
            else:
                messages.error(request,'Nedovoljno kabela')
                context = {'queryset':queryset,'form':form}
                return  render(request, 'forma.html', context)
            # kopiranje odabranog objekta u history
            history = CijevHistory.objects.create(
                #id = instance.id,
                inv_broj = instance.inv_broj,
                naziv = instance.naziv,
                proizvodjac = instance.proizvodjac,
                vlasnik = instance.vlasnik,
                vrsta_cijevi = instance.vrsta_cijevi,
                promjer = instance.promjer,
                metraza = instance.metraza,
                izdana_metraza = instance.izdana_metraza,
                izdano_na = instance.izdano_na,
                izdao = instance.izdao,
                radnja = instance.radnja,
                zadnje_osvjezeno = instance.zadnje_osvjezeno,
            )
            history.save()

            return redirect('skladiste_app:cijevi_detalji', pk)

    context = {'queryset':queryset,
                'form':form,
                'username': 'Izdao: '+str(request.user)
    }

    return  render(request, 'forma.html', context)


@login_required
def cijev_obrisi(request, pk):
    queryset = Cijev.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('skladiste_app:listcijevi')
    return render(request, 'obrisi_artikl.html')

@login_required
def cijev_reorder_level(request, pk):
    queryset = Cijev.objects.get(id=pk)
    form = CijevReorderLevelForm(request.POST or None, instance = queryset)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Nivo naručivanja za ' + str(instance.naziv) + ' postavljen je na ' + str(instance.reorder_level) + '.')

            return redirect('skladiste_app:cijevi_detalji', pk)

    context = {'instance': queryset, 'form': form}
    return render (request, 'forma.html', context)

@login_required
def cijev_history(request):
    form = CijevHistorySearchForm(request.POST)
    queryset = CijevHistory.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        queryset = CijevHistory.objects.filter(naziv__icontains = form['naziv'].value(),
                                            inv_broj__icontains = form['inv_broj'].value(),
                                            proizvodjac__icontains = form['proizvodjac'].value(),
                                            #tip_kabela__icontains = form['tip_kabela'].value(),
                                            vlasnik__icontains = form['vlasnik'].value(),
                                            promjer__icontains = form['promjer'].value(),
                                            #izdano_na__icontains = form['izdano_na'].value(),
                                            radnja__icontains = form['radnja'].value()
        )
        
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['NAZIV', 'INVENTURNI BROJ', 'TIP KABELA', 'VLASNIK','PROMJER','PROIZVOĐAČ'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.naziv, stock.inv_broj, stock.tip_kabela, stock.vlasnik, stock.promjer, stock.proizvodjac])

            return response
        else:

            context = {'form':form, 'queryset':queryset}

    return render(request, 'cijevihistory.html', context)
###########################

#MATERIJAL

@login_required
def listmaterijal(request):
    form = MaterijalSearchForm(request.POST)
    queryset = Materijal.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        #tip_kabela = (form['tip_kabela'].value)
        queryset = Materijal.objects.filter(naziv__icontains = form['naziv'].value(),
                                            inv_broj__icontains = form['inv_broj'].value(),
                                           # vlasnik__icontains = form['vlasnik'].value(),
        )
        #if (tip_kabela != ''):
        #    queryset = queryset.filter(tip_kabela_id = tip_kabela)

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['NAZIV', 'INVENTURNI BROJ', 'VLASNIK',])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.naziv, stock.inv_broj, stock.vlasnik])

            return response
        else:

            context = {'form':form, 'queryset':queryset}
    
    return render(request,'skladistematerijal.html', context )


@login_required
def materijal_dodaj(request):
    queryset = Materijal.objects.all()
    form = MaterijalCreateForm()

    if request.method =='POST':
        form = MaterijalCreateForm(request.POST)
        if form.is_valid():
            kreirao = str(request.user)
            form.save()
            messages.success(request, 'Uspješno dodano!')
            return redirect('skladiste_app:listmaterijal')

    context = {'form': form, 'queryset':queryset}
    return render(request, 'forma.html', context)





@login_required
def materijal_detalji(request, pk):
    queryset = Materijal.objects.get(id=pk)
    context = {'queryset':queryset}
    
    return render(request, 'materijal_detalji.html', context)

@login_required
def materijal_uredi(request, pk):
	queryset = Materijal.objects.get(id=pk)

	form = MaterijalUpdateForm(instance = queryset)

	if request.method == 'POST':
		form = UtpUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('skladiste_app:materijal_detalji', pk)

	context = {'form':form}

	return render(request, 'forma.html', context)


@login_required
def materijal_izdaj(request, pk):
    queryset = Materijal.objects.get(id=pk)
    form = MaterijalIzdajForm()

    if request.method =='POST':
        form = MaterijalIzdajForm(request.POST, instance=queryset)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.kolicina -= instance.izdana_kolicina
            if (instance.kolicina >=0):
                instance.izdao = str(request.user)
                messages.success(request, 'Uspješno izdano. Još ' + str(instance.kolicina) + ' komada ostalo na skladištu.')
                instance.save()
            else:
                messages.error(request,'Nedovoljno na skladištu.')
                context = {'queryset':queryset,'form':form}
                return  render(request, 'forma.html', context)
            # kopiranje odabranog objekta u history
            history = MaterijalHistory.objects.create(
                #id = instance.id,
                inv_broj = instance.inv_broj,
                naziv = instance.naziv,
                vlasnik = instance.vlasnik,
                kolicina = instance.kolicina,
                izdana_kolicina = instance.izdana_kolicina,
                izdano_na = instance.izdano_na,
                izdao = instance.izdao,
                radnja = instance.radnja,
                zadnje_osvjezeno = instance.zadnje_osvjezeno,
            )
            history.save()

            return redirect('skladiste_app:materijal_detalji', pk)

    context = {'queryset':queryset,
                'form':form,
                'username': 'Izdao: '+str(request.user)
    }

    return  render(request, 'forma.html', context)


@login_required
def materijal_obrisi(request, pk):
    queryset = get_object_or_404(Materijal,id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('skladiste_app:listmaterijal')
    return render(request, 'obrisi_artikl.html')

@login_required
def materijal_reorder_level(request, pk):
    queryset = Materijal.objects.get(id=pk)
    form = MaterijalReorderLevelForm(request.POST or None, instance = queryset)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Nivo naručivanja za ' + str(instance.naziv) + ' postavljen je na ' + str(instance.reorder_level) + '.')

            return redirect('skladiste_app:materijal_detalji', pk)

    context = {'instance': queryset, 'form': form}
    return render (request, 'reorder_level.html', context)

@login_required
def materijal_history(request):
    form = UtpHistorySearchForm(request.POST)
    queryset = MaterijalHistory.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        queryset = KabelUtpHistory.objects.filter(naziv__icontains = form['naziv'].value(),
                                            inv_broj__icontains = form['inv_broj'].value(),
                                            vlasnik__icontains = form['vlasnik'].value(),
                                            radnja__icontains = form['radnja'].value()
        )
        
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['NAZIV', 'INVENTURNI BROJ','VLASNIK'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.naziv, stock.inv_broj, stock.vlasnik,])

            return response
        else:

            context = {'form':form, 'queryset':queryset}

    return render(request, 'materijalhistory.html', context)


#ALAT

@login_required
def listalat(request):
    form = AlatSearchForm(request.POST)
    queryset = Alat.objects.all()
    context = {'queryset':queryset, 'form':form}
    
    
    if request.method == 'POST':
        queryset = Materijal.objects.filter(inv_broj__icontains = form['inv_broj'].value(),
                                            naziv__icontains = form['naziv'].value(),
                                            proizvodjac__icontains = form['proizvodjac'].value(),
                                            sr_broj__icontains = form['sr_broj'].value(),
        )
        

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="skladiste_lista.csv"'

            response.write(u'\ufeff'.encode('utf8')) #pravilan prikaz znakova
            writer = csv.writer(response) 
            writer.writerow(['INVENTURNI BROJ','NAZIV', 'PROIZVOĐAČ','SERIJSKI BROJ','ZADUŽIO'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.inv_broj, stock.naziv, stock.proizvodjac, stock.sr_broj, stock.zaduzio])

            return response
        else:

            context = {'form':form, 'queryset':queryset}
    
    return render(request,'skladistealat.html', context )


@login_required
def alat_dodaj(request):
    queryset = Alat.objects.all()
    form = ALatCreateForm()

    if request.method =='POST':
        form = ALatCreateForm(request.POST)
        if form.is_valid():
            novo = form.save(commit=False)
            novo.kreirao = request.user
            novo.save()
            messages.success(request, 'Uspješno dodano!')
            return redirect('skladiste_app:listalat')

    context = {'form': form, 'queryset':queryset}
    return render(request, 'dodaj.html', context)





@login_required
def alat_detalji(request, pk):
    queryset = Alat.objects.get(id=pk)
    context = {'queryset':queryset}
    
    return render(request, 'alat_detalji.html', context)

@login_required
def alat_uredi(request, pk):
	queryset = Alat.objects.get(id=pk)

	form = AlatUpdateForm(instance = queryset)

	if request.method == 'POST':
		form = AlatUpdateForm(request.POST, instance = queryset)
		if form.is_valid():
			form.save()
			return redirect('skladiste_app:alat_detalji', pk)

	context = {'queryset':queryset, 'form':form}

	return render(request, 'forma.html', context)


@login_required
def alat_zaduzi(request, pk):
    queryset = Alat.objects.get(id=pk)
    form = AlatZaduziForm()

    if request.method =='POST':
        form = AlatZaduziForm(request.POST, instance=queryset)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.izdao = str(request.user)
            messages.success(request, 'Uspješno izdano.')
            instance.save()
            
            return redirect('skladiste_app:alat_detalji', pk)

    context = {'queryset':queryset,
                'form':form,
                'username': 'Izdao: '+str(request.user)
    }

    return  render(request, 'forma.html', context)

@login_required
def alat_obrisi(request, pk):
    queryset = get_object_or_404(Alat,id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('skladiste_app:listalat')
    return render(request, 'obrisi_artikl.html')
#################################

#SKLADISTE DASH
@login_required
def skladiste(request):
    optika = KabelOptika.objects.all()
    bakar = KabelBakar.objects.all()
    utp = KabelUtp.objects.all()
    cijevi = Cijev.objects.all()
    materijal = Materijal.objects.all()
    alat = Alat.objects.all()

    context = {'optika':optika,
                'bakar':bakar,
                'utp':utp,
                'cijevi':cijevi,
                'materijal':materijal,
                'alat':alat
    }

    
    return render(request,'skladiste.html', context )
