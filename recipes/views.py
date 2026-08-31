#Função do render é ler o arquivo e renderizar ele
from django.shortcuts import render
from utils.recipes.main import make_recipe
# Create your views here.
#cliente faz HTTp request
#servidor return Http response


# tem que dar namespace para arquivos de template
def home(request):#Essa string é o caminho até o html
    return render(request, 'recipes/pages/home.html', status= 200, context={
        # uma lista que gera 10 receitas com o make que cria coisas fake
        'recipes': [make_recipe() for _ in range(10)]
    })
    #Adiciona a pasta e depois o arquivo que está na pasta


# tem que dar namespace para arquivos de template
def recipe(request,dinamico):#Essa string é o caminho até o html
    return render(request, 'recipes/pages/recipe-view.html', status= 200, context={
        'recipe': make_recipe(),
        'isdetail_page': True,
    })
    #Adiciona a pasta e depois o arquivo que está na pasta