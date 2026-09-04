from django.contrib import admin
# import da Category que foi criada no models
from . models import Category,Recipe
# Registrar os models.
# criar models parte de ORM - parte de dados

'''
Duas formas de registrar models
com decorator
@admin.register
----------------------------
mais simples
admin.site.register

para criar precisa criar a classe admin
'''

class CategoryAdmin(admin.ModelAdmin):
    pass


'''
Cria a classe da mesma forma que a outra e usa o decorador
'''
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass

'''
Cria a classe depois passa a forma de criar admin
passa no parametro simples: Passa a classe criada no models e depois a classe criada aqui no admin
'''
admin.site.register(Category,CategoryAdmin)


