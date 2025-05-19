from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='services') # upload_to crea un directorio si no existe y sube siempre las imagenes en donde especifiquemos
    # Este de aca solo se ejecuta la primera vez
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    # Y este cada vez que se ejecute o se haga un update
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        # Aca devolvemos el nombre del titulo para que a la hora de verlo en el panel de admin
        # Aparezca ese nombre en lugar de Project Object
        return self.title