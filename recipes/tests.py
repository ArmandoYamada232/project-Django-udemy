from django.test import TestCase
from django.urls import reverse
# Reverse serve para analisar a url de dentro para fora e testar
# Create your tests here.
# Nome do teste tem que ser muito descritivo
# Todo metodo dessa classe que começa com teste_ é considerado um test

# Usa-se o self.assert
# checar se a url da home é a barra
# Se a home_url é igual a barra usa-se o assertEqual
    
# url = reverse('recipes:category', args=(1,))
# url = reverse('recipes:category', kwargs={'id': 1})
class RecipeURLsTest(TestCase):   
    def test_recipe_home_urls_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')
        
    def test_recipe_category_urls_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')
        
    def test_recipe_detail_urls_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')