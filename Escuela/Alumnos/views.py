
from django.views.generic import ListView, CreateView,DeleteView
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


def update_alumno(request,pk):

    if  request.method == 'GET':
        alumno = Alumnos.objects.get(id=pk)
        context = {
            'form' : AlumnosForm(
                initial = {
                    'name' : alumno.name,
                    'age' : alumno.age,
                    'activo' : alumno.activo,
                }
            )
        }
        return render(request, 'Alumno/update_alumno.html', context=context)

    elif request.method == 'POST':
        form = AlumnosForm(request.POST)
        alumno = Alumnos.objects.get(id=pk)
        if form.is_valid():
            alumno.name = form.cleaned_data['name']
            alumno.age = form.cleaned_data['age']
            alumno.activo = form.cleaned_data['activo']
            alumno.save()

            context={
                'message': 'Alumno actualizado exitosamente'
            }
        else:
                context= {
                'form_errors': form.erros,
                'form' : AlumnosForm()
            }
        return render(request, 'Alumno/update_alumno.html', context=context)


class AlumnosDeleteView(DeleteView):
    model = Alumnos
    template_name = 'Alumno/delete_alumno.html'
    success_url = '/Alumnos/list_alumno/'





























class AlumnosCreateView(CreateView):
    model = Alumnos
    template_name = 'Alumno/create_alumno.html'
    fields = '__all__'
    success_url = 'Alumno/list_alumno.html'

class AlumnosListViews(ListView):
    model= Alumnos
    template_name = 'Alumno/list_alumno.html'
    queryset = Alumnos.objects.filter(activo = True)