from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    # Este de aca solo se ejecuta la primera vez
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    # Y este cada vez que se ejecute o se haga un update
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created']

    def __str__(self):
        # Aca devolvemos el nombre del titulo para que a la hora de verlo en el panel de admin
        # Aparezca ese nombre en lugar de Project Object
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null= True, blank= True) # upload_to crea un directorio si no existe y sube siempre las imagenes en donde especifiquemos
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorias', related_name='get_posts')
    # Este de aca solo se ejecuta la primera vez
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    # Y este cada vez que se ejecute o se haga un update
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']

    def __str__(self):
        # Aca devolvemos el nombre del titulo para que a la hora de verlo en el panel de admin
        # Aparezca ese nombre en lugar de Project Object
        return self.title