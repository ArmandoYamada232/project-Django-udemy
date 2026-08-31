from django.urls import path

#caminho('rota/', função)
#from (da) . (pasta que eu to) import views
from . import views
#importa as views que está dentro da pasta recipes(meu app) o modulo inteiro
# urls e views está dentro do modulo também 

#quando for importar usar o namespace do modulo (views.função)

# usa-se recipes:recipe
app_name = 'recipes'

urlpatterns = [
    path('',views.home, name='home'),
    #declara antes do id o formato que eu quero e dentro do maior e menor, slug, int, string entre outros
    #int:
    # para dar um nome único para a url dinamica utiliza-se o name
    # esse name são nome correto e único das urls
    path('recipes/<int:dinamico>/', views.recipe, name = 'recipe'),
]