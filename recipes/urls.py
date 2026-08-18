from django.http import HttpResponse
from recipes.views import home, contato,sobre
from django.urls import path
#caminho('rota/', função)


urlpatterns = [
    path('sobre/', sobre),
    path('home/',home ),
    path('contato/', contato)
]