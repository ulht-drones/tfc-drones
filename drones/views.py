from django.shortcuts import render
from .models import Celula

# Create your views here.
def view_index(request):
    return render(request, 'drones/index.html')


def view_mapa(request):

    context = {
        'celulas': Celula.objects.all()
    }

    return render(request, 'drones/mapa.html', context)