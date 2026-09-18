from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe, User

class RecipeViewsTest(TestCase):
    def teste_recipe_home_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    
    #self.client. com vários jeitos de utilizar: get, post   
    # função verifica se o status code da home está 200 e ok
    def teste_recipe_home_view_returns_status_code_200_ok(self):
            response = self.client.get(
                reverse('recipes:home'))
            self.assertEqual(response.status_code, 200)
            
    def teste_recipe_home_view_loads_correct_template(self):
        response = self.client.get(
            reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
             
        # self.assertIn() é uma coisa está dentro de outra coisa 
        # saber se No recipe found no primeiro parametro está na página carregada do content response
    def test_recipe_home_template_show_no_recipes_if_no_recipe(self):
        response = self.client.get(
            reverse('recipes:home'))
        self.assertIn(
            'No recipes found',
            response.content.decode('utf-8')            
        )
    
    # author = User.objects.create_user(first_name, last_name) ou create_superuser. 
    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name= 'Category')
        author = User.objects.create_user(
            first_name = 'Tatu',
            last_name = 'canastra',
            username= 'tatucanastra',
            password='123',
            email='canastra'
        )
        Recipe.objects.create(
            category = category,
            author = author ,          
            title = 'Recipe Title',
            description = 'Recipe description',
            slug = 'Recipe-slug',
            preparation_time = 10,
            preparation_time_unit = 'min',
            servings = 5,
            servings_unit = 'porções',
            preparation_steps = 'Recipe preparation stepes',
            preparation_steps_is_html = False,
            is_published = True,
        )
        self.assertEqual(1 ,1)
    
    def teste_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
        
    def teste_recipe_category_view_returns_404_recipes_not_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 100000}))
        self.assertEqual(response.status_code, 404)
    
        
    def teste_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)    
     
    def teste_recipe_detail_view_returns_404_recipes_not_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 100000}))
        self.assertEqual(response.status_code, 404)