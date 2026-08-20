from recipes.views import home
from django.urls import path
#caminho('rota/', função)


urlpatterns = [
    path('',home ),
]