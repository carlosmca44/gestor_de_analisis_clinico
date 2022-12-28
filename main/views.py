from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required
def home(request):
    context = {}
    return render(request, 'home/home.html', context)


@login_required
def createUser(request):
    if request.method == 'POST':
        form = userCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = userCreationForm()

    context = {'form': form}
    return render(request, 'users/createUser.html', context)


def clinicalAnalysis(request):
    context = {}
    return render(request, 'clinical-analysis-request/list.html', context)


def pacients(request):
    pacients = Pacient.objects.all()
    context = {'pacients': pacients}
    return render(request, 'pacients/list.html', context)


def newPacient(request):
    if request.method == 'POST':
        form = newPacientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pacients')
    else:
        form = newPacientForm()

    context = {'form': form}
    return render(request, 'pacients/newPacient.html', context)


def editPacient(request, pacientId):
    pacient = Pacient.objects.get(id=pacientId)
    if request.method == 'POST':
        form = newPacientForm(request.POST, instance=pacient)
        if form.is_valid():
            form.save()
            return redirect('pacients')
    else:
        form = newPacientForm(instance=pacient)

    context = {'form': form}
    return render(request, 'pacients/editPacient.html', context)


def deletePacient(_request, pacientId):
    Pacient.objects.get(id=pacientId).delete()
    return redirect('pacients')
