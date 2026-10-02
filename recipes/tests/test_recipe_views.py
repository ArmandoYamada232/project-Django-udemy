from django.urls import reverse, resolve
from recipes import views
from .teste_recipe_base import RecipeTestBase
from unittest import skip

# para skippar teste usa-se: from unittest import skip
# e decorar a classe com @skip('Mensagem do porque estou')

# setup é responsável por ser executado antes dos testes e o teardown
# depois do teste cada um teste vai ter o setup e teardown

#tenho que escrever mais algumas coisas sobre o teste
#self.fail('Para que eu termine de digitá-lo')

class RecipeViewsTest(RecipeTestBase):
    #setup
    def teste_recipe_home_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    #teardown

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
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1> No recipes found </h1>',
            response.content.decode('utf-8')            
    )


    def test_recipe_home_template_loads_recipes_a(self):
        self.make_recipe(author_data = {
            'first_name': 'joaozinho',
        })
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        
        self.assertIn('Recipe Title', content)
        self.assertIn('10 min', content)
        self.assertIn('5 porções', content)
        self.assertIn('joaozinho', content)
        self.assertEqual(len(response_context_recipes), 1)
        #tenho que escrever mais algumas coisas sobre o teste
        #self.fail('Para que eu termine de digitá-lo')
    
    def test_recipe_category_template_loads_recipes_a(self):
            
        needed_Title = 'this is a category test'
        self.make_recipe(title= needed_Title)

        response = self.client.get(reverse('recipes:category', args= (1,)))
        content = response.content.decode('utf-8')
            
        self.assertIn(needed_Title, content)


    def test_recipe_home_template_do_not_loads_recipe_is_published(self):
            
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        # Se modificar o h1 lá vai quebrar dois testes
        self.assertIn(
            '<h1> No recipes found </h1>', response.content.decode('utf-8')
        )

    def teste_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
        
    def teste_recipe_category_view_returns_404_recipes_not_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 100000}))
        self.assertEqual(response.status_code, 404)
    

    def test_recipe_category_template_do_not_loads_recipe_is_published(self):
                
        recipe = self.make_recipe(is_published=False)
    
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id})
        )
        self.assertEqual(response.status_code, 404)

    def teste_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)    
     
    def teste_recipe_detail_view_returns_404_recipes_not_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 100000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()

        #print(Recipe.objects.all())
    
        response = self.client.get(reverse('recipes:home'))

    def test_recipe_detail_template_loads_the_correct_recipes_a(self):
        needed_Title = 'this is a detail page - load one recipe'

        # need a recipe for this test
        self.make_recipe(title= needed_Title)

        response = self.client.get(
            reverse('recipes:recipe', kwargs= {'id':1}))

        content = response.content.decode('utf-8')
        #Sempre usar Utf-8
            
        self.assertIn(needed_Title, content)


    def test_recipe_detail_template_do_not_loads_recipe_is_published(self):
                    
        recipe = self.make_recipe(is_published=False)
        
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.category.id})
        )
        self.assertEqual(response.status_code, 404)