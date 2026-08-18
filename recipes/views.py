from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('Essa é a home.')

def contato(request):
    return HttpResponse('Essa é a contato.')

#cliente faz HTTp request
def sobre(request):
    #servidor return Http response
    return HttpResponse('Esse é o sobre')
