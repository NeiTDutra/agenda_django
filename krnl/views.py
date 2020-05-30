from django.shortcuts import render
from krnl.models import Evento


# Create your views here.

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)
