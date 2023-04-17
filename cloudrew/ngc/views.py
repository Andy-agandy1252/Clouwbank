from django.shortcuts import render
from .models import Projektas, Klient, Worker, Job, Account

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
def index(request):
    num_projects = Projektas.objects.all().count()
    num_klients = Klient.objects.all().count()
    num_workers = Worker.objects.all().count()
    num_jobs = Job.objects.all().count()
    num_accounts = Account.objects.all().count()
    context  ={
        'num_projects': num_projects,
        'num_klients': num_klients,
        'num_workers': num_workers,
        'num_jobs': num_jobs,
        'num_accounts': num_accounts,
    }
    return render(request, 'index.html', context=context)

def Projektai(request):
    projektai = Projektas.objects.all()
    context = {
        'projektai': projektai
    }
    return render(request, 'projektai.html', context=context)


def projektas(request, projektas_id):
    single_projektas = get_object_or_404(Projektas, pk=projektas_id)
    return render(request, 'projektas.html', {'projektas': single_projektas})

def Klijentai(request):
    klijentai = Klient.objects.all()
    context = {
        'klijentai': klijentai
    }
    return render(request, 'klijentai.html', context=context)

def Darbuotojai(request):
    darbuotojai = Worker.objects.all()
    context = {
        'darbuotojai': darbuotojai
    }
    return render(request, 'darbuotojai.html', context=context)

def Darbai(request):
    darbai = Job.objects.all()
    context = {
        'darbai': darbai
    }
    return render(request, 'darbai.html', context=context)

def Saskaitos(request):
    saskaitos = Account.objects.all()
    context = {
        'saskaitos': saskaitos
    }
    return render(request, 'saskaitos.html', context=context)



