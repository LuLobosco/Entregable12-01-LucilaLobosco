
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DeleteView
from Profesores.models import Profesores
from Profesores.forms import ProfesorForm

def create_profesor(request):
    if request.method == 'GET':
        context = {
            'form' : ProfesorForm()
        }
        return render(request, 'Profesores/create_profesores.html', context=context)

    elif request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            Profesores.objects.create(
                name = form.cleaned_data['name'],
                age = form.cleaned_data['age'],
                Materia = form.cleaned_data['Materia'],
                activo = form.cleaned_data['activo']
            )
            return render(request, 'Profesores/create_profesores.html', context={})
        else:
            context={
                'form_errors': form.erros,
                'form' : ProfesorForm()
            }
            return render(request, 'Profesores/create_profesores.html', context=context)



def list_profesor(request):
    if 'search' in request.GET:
        search = request.GET['search']
        profesor = Profesores.objects.filter(name__contains = search)
    else:
        profesor = Profesores.objects.all()
    context = {
        'profesor': profesor,
    }
    return render(request,'Profesores/list_profesores.html', context = context )
    

def update_profesor(request,id):

    if  request.method == 'GET':
        Profesor = Profesores.objects.get(id=id)
        context = {
            'form' : AdministrativoForm(
                initial = {
                    'name' : Profesor.name,
                    'age' : Profesor.age,
                    'activo' : Profesor.activo,
                }
            )
        }
        return render(request, 'Profesores/update_profesor.html', context=context)

    elif request.method == 'POST':
        form = ProfesorForm(request.POST)
        Profesor = Profesores.objects.get(id=id)
        if form.is_valid():
            Profesores.name = form.cleaned_data['name']
            Profesores.age = form.cleaned_data['age']
            Profesores.activo = form.cleaned_data['activo']
            Profesores.save()

            context={
                'message': 'Profesor actualizado exitosamente'
            }
        else:
                context= {
                'form_errors': form.erros,
                'form' : ProfesorForm()
            }
        return render(request, 'Profesor/update_profesor.html', context=context)

class ProfesorDeleteView(DeleteView):
    model = Profesores
    template_name = 'Profesores/delete_profesor.html'
    success_url = '/Profesores/list_profesor/'
