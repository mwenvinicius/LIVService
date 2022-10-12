from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def services(request):
    context = {
        'mensagem':'Olá, tudo bem? Você está na página de serviços.'
    }
    return render(request, 'services/services.html', context)

def service(request, pk):
    return render(request, 'services/single-service.html')
