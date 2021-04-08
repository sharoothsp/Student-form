from django.shortcuts import render, redirect
import requests
from .models import Sprofile
from .forms import SprofileForm, Searchform

# Create your views here.


def index(request):
    if request.method == 'POST':
        return redirect('profiles')

    context = {
    'abc':'welcome'

    }
    return render(request, 'home.html',context)

def profiles(request):
    if request.method == 'POST':

        newform = SprofileForm(request.POST)
        newform.save()
        return redirect('home')
    else:
        newform = SprofileForm()
    context = {
    'form':newform
    }
    return render(request, 'profile.html', context)


def details(request):
    if request.method == 'POST':
        searchform = Searchform(request.POST or None)
        if searchform.is_valid():
            sname = searchform.cleaned_data.get("search")
        D=Sprofile.objects.filter(First_name=sname)
    else:
        searchform = Searchform
        D = None

    context = {
    'Sform' : searchform,
    'D' : D,
    }
    return render(request,'details.html', context)

"""
def profiles(request):
    if request.method == 'POST':
        First_name = request.POST.get('fname')
        print(First_name)
        obj = Sprofile.objects.create(First_name=First_name)
        obj.save()
        s = Sprofile.objects.get(id=18)
        print(s.First_name)

    context = {

    }
    return render(request, 'profile.html', context)
"""
