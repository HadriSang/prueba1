from django.db import models

# Create your models here.
class Link(models.Model):
    # Los campos SlugField nos permite usar caracteres alfanumericos es decir, nada de espacios ni caracteres especiales.
    key= models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True)
    name= models.CharField(verbose_name='Red social',  max_length=100)
    url= models.URLField(verbose_name='Enlace',  max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering= ['name']

    def __str__(self):
        return self.name


