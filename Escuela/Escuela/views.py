from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse 
from django.shortcuts import render,redirect
from index.models import ImageIndex


def index(request):
    all_pictures = ImageIndex.objects.all
    context = {
        'pictures': all_pictures,
    }
    return render(request,'index.html',context={})

def Acerca_de_mi(request):
    return render(request,'Acerca_de_mi.html',context={})

