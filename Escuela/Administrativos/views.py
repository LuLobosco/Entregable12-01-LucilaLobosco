from django.shortcuts import render
from django.http import HttpResponse

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

