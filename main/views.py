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
