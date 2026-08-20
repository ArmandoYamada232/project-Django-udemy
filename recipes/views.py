#Função do render é ler o arquivo e renderizar ele
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# tem que dar namespace para arquivos de template
def home(request):#Essa string é o caminho até o html
    return render(request, 'recipes/home.html', status= 200, context={
        'name': 'Armando',
    })
    #Adiciona a pasta e depois o arquivo que está na pasta

def contato(request):
    return render(request, 'recipes/contato.html')

#cliente faz HTTp request
def sobre(request):
    #servidor return Http response
    return render(request, 'recipes/sobre.html')
