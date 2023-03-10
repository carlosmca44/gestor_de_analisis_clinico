from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import userCreationForm, newPacientForm, newClinicalAnalysisForm, ResultsForm
from .models import User, Pacient, AnalysisRequest, Results


@login_required
def home(request):

    # Doctor
    pacients = Pacient.objects.all()

    # Lab
    analysisLab = AnalysisRequest.objects.filter(done=False)

    # Bio
    analysisBio = AnalysisRequest.objects.filter(denied=False, done=True)

    context = {'analysis': analysisLab,
               'pacients': pacients, 'analysisBio': analysisBio}
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


def clinicalAnalysis(request):
    analysis = AnalysisRequest.objects.all()
    context = {'analysis': analysis}
    return render(request, 'clinical-analysis-request/list.html', context)


def newClinicalAnalysis(request):
    if request.method == 'POST':
        form = newClinicalAnalysisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinicalAnalysis')
    else:
        form = newClinicalAnalysisForm()

    context = {'form': form}
    return render(request, 'clinical-analysis-request/new-clinical-analysis.html', context)


def editClinicalAnalysis(request, analysisId):
    analysis = AnalysisRequest.objects.get(id=analysisId)
    if request.method == 'POST':
        form = newClinicalAnalysisForm(request.POST, instance=analysis)
        if form.is_valid():
            form.save()
            return redirect('clinicalAnalysis')
    else:
        form = newClinicalAnalysisForm(instance=analysis)

    context = {'form': form}
    return render(request, 'clinical-analysis-request/editAnalysis.html', context)


def deleteClinicalAnalysis(_request, analysisId):
    AnalysisRequest.objects.get(id=analysisId).delete()
    return redirect('clinicalAnalysis')


def newResult(request):
    if request.method == 'POST':
        form = ResultsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinicalAnalysis')
    else:
        form = ResultsForm()

    context = {'form': form}
    return render(request, 'results/newResult.html', context)


def setAnalysisDone(_request, analysisId):
    AnalysisRequest.objects.filter(id=analysisId).update(done=True)
    if AnalysisRequest.objects.get(id=analysisId).denied == True:
        AnalysisRequest.objects.filter(id=analysisId).update(denied=False)
    return redirect('home')


def setAnalysisDenied(_request, analysisId):
    AnalysisRequest.objects.filter(
        id=analysisId).update(done=False, denied=True)
    return redirect('home')
