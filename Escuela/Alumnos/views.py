
from django.shortcuts import render
from django.http import HttpResponse

from Alumnos.models import Alumnos
from Alumnos.forms import AlumnosForm

def create_alumno(request):
    if request.method == 'GET':
        context = {
            'form' : AlumnosForm()
        }
        return render(request, 'Alumno/create_alumno.html', context=context)

    elif request.method == 'POST':
        form = AlumnosForm(request.POST)
        if form.is_valid():
            Alumnos.objects.create(
                name = form.cleaned_data['name'],
                age = form.cleaned_data['age'],
                activo = form.cleaned_data['activo']
            )
            return render(request, 'Alumno/create_alumno.html', context={})
        else:
            context={
                'form_errors': form.erros,
                'form' : AlumnosForm()
            }
            return render(request, 'Alumno/create_alumno.html', context=context)



def list_alumno(request):
    if 'search' in request.GET:
        search = request.GET['search']
        alumno = Alumnos.objects.filter(name__contains = search)
    else:
        alumno = Alumnos.objects.all()
    context = {
        'alumno': alumno,
    }
    return render(request,'Alumno/list_alumno.html', context = context )
