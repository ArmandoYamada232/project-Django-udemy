from django.test import TestCase
from recipes.models import Category, Recipe, User

class RecipeTestBase(TestCase):
    def setUp(self):
        return super().setUp()

    def make_recipe(
        self,
        category_data = None,
        author_data = None,          
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
    ):
        if category_data is None:
            category_data = {}
        
        if author_data is None:
            author_data = {}   
        
        #(**category_data) desempacotar serve para pegar todas as chaves do dicionário e criar   
        return Recipe.objects.create(
            category = self.make_category(**category_data),
            author = self.make_author(**author_data),          
            title = title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published =  is_published,
        )

    def make_author(
        self,
        first_name = 'tatu',
        last_name = 'canastra',
        username= 'tatucanastra',
        password='123',
        email='canastra'       
        ):

        return User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email= email
        )

    def make_category(self, name = 'Category'):
        return Category.objects.create(name = name)
        