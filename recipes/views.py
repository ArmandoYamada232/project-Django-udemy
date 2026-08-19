#Função do render é ler o arquivo e renderizar ele
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# tem que dar namespace para arquivos de template
def home(request):#Essa string é o caminho até o html
    return render(request, 'recipes/home.html')
    #Adiciona a pasta e depois o arquivo que está na pasta

def contato(request):
    return HttpResponse('Essa é a contato.')

#cliente faz HTTp request
def sobre(request):
    #servidor return Http response
    return HttpResponse('Esse é o sobre')
