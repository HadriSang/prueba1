from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')
    list_display= ('title', 'author', 'published','post_categories' )
    ordering= ('author', 'published')
    # con esto creamos la barra de busqueda y dentro de la tupla definimos los campos por los cuales realizara la busqueda
    #pero con algunos es necesario usar una sintaxis diferente como el author
    search_fields =('title', 'content', 'categories__name' ,'author__username') # con el __username le decimos que en el objeto author busque el campo username
    date_hierarchy = 'published'
    list_filter= ('categories__name' ,'author__username')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description='Categorias'
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
