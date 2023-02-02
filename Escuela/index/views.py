from django.shortcuts import render,redirect
from django.views.generic import ListView
from index.models import ImageIndex

#class ImageListViews(ListView):
#    model= ImageIndex
#    template_name = 'index.html'

def list_index(request):
    all_pictures = ImageIndex.objects.all
    context = {
        'pictures': all_pictures,
    }
    return render(request,'Index.html', context = context )