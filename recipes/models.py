from django.db import models

# Create your models here.
# para criar é escrever basicamente uma classe

# "tabela"
class recipe(models.Model):
    # os atributos da classe são as colunas
    title = models.CharField(max_length=65) #Equivalente ao varchar do DB
    description = models.CharField(max_length=166)
    '''
    slug é um campo especial de identificador usado normalmente em urls para representar um objeto
    no caso aqui ele vai ser utilizado para achar uma determinada receita
    '''
    slug = models.SlugField(_(""))
    preparation_time = models.IntegerField() #para inteiros
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField() #esse é bom para textos grandes
    preparation_steps_is_html = models.BooleanField(default=False) #campo de escolhas ou é True ou False
    created_at = models.DateTimeField(auto_now_add=True) #no momento da criação quer que gere uma data da criação
    #updated_at mostra somente a data que foi atualizado
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    #image field campo para imagens na pasta recipes/covers com data
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    #category = 
    #author = 
