#Função do render é ler o arquivo e renderizar ele
#ctrl + space mostra um auto complete
# get_list_or_404 - Busca uma lista e se não achar retorna 404
# get_object_or_404 - Busca um elemento e se não achar retorna o 404
from django.shortcuts import render,get_list_or_404,get_object_or_404
from utils.recipes.main import make_recipe
from recipes.models import Recipe
from django.http import Http404
#from django.http import HttpResponse

# Create your views here.
# cliente faz HTTp request
# servidor return Http response


# tem que dar namespace para arquivos de template
def home(request):#Essa string é o caminho até o html
    #usa objects.all para buscar todas as receitas
    recipes = Recipe.objects.filter(
        is_published = True).order_by('-id')
    return render(request, 'recipes/pages/home.html', status= 200, context={
        # uma lista que gera 10 receitas com o make que cria coisas fake
        'recipes': recipes,
    })
    #Adiciona a pasta e depois o arquivo que está na pasta

def recipe(request,id):
    return render(request, 'recipes/pages/recipe-view.html', status= 200, context={
        'recipe': make_recipe(),
        'isdetail_page': True,
    })

    
def category(request,category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id = category_id, is_published = True,
        ).order_by('-id')
    )
    return render(request, 'recipes/pages/category.html', status= 200, context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category |'
    })
    