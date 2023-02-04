from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DeleteView
from Administrativos.models import Administrativos
from Administrativos.forms import AdministrativoForm

def create_administrativo(request):
    if request.method == 'GET':
        context = {
            'form' : AdministrativoForm()
        }
        return render(request, 'Administrativos/create_administrativo.html', context=context)

    elif request.method == 'POST':
        form = AdministrativoForm(request.POST)
        if form.is_valid():
            Administrativos.objects.create(
                name = form.cleaned_data['name'],
                age = form.cleaned_data['age'],
                activo = form.cleaned_data['activo']
            )
            return render(request, 'Administrativos/create_administrativo.html', context={})
        else:
            context={
                'form_errors': form.erros,
                'form' : AdministrativoForm()
            }
            return render(request, 'Administrativos/create_administrativo.html', context=context)



def list_administrativo(request):
    if 'search' in request.GET:
        search = request.GET['search']
        administrativo = Administrativos.objects.filter(name__contains = search)
    else:
        administrativo = Administrativos.objects.all()
    context = {
        'administrativo': administrativo,
    }
    return render(request,'Administrativos/list_administrativo.html', context = context )

def update_administrativo(request,pk):

    if  request.method == 'GET':
        administrativo = Administrativos.objects.get(id=pk)
        context = {
            'form' : AdministrativoForm(
                initial = {
                    'name' : administrativo.name,
                    'age' : administrativo.age,
                    'activo' : administrativo.activo,
                }
            )
        }
        return render(request, 'Administrativos/update_administrativo.html', context=context)

    elif request.method == 'POST':
        form = AdministrativoForm(request.POST)
        administrativo = Administrativos.objects.get(id=pk)
        if form.is_valid():
            administrativo.name = form.cleaned_data['name']
            administrativo.age = form.cleaned_data['age']
            administrativo.activo = form.cleaned_data['activo']
            administrativo.save()

            context={
                'message': 'Administrativo actualizado exitosamente'
            }
        else:
                context= {
                'form_errors': form.erros,
                'form' : AdministrativoForm()
            }
        return render(request, 'Administrativos/update_administrativo.html', context=context)

class AdministrativoDeleteView(DeleteView):
    model = Administrativos
    template_name = 'Administrativos/delete_administrativo.html'
    success_url = '/Administrativos/list_administrativo/'