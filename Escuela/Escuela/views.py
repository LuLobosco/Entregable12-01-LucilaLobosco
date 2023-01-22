from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return render(request,'index.html',context={})

def Acerca_de_mi(request):
    return render(request,'Acerca_de_mi.html',context={})