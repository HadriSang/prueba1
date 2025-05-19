from django.shortcuts import render, get_object_or_404
from .models import Post, Category
# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})

def category(request, category_id):
    # El get nos permite recoge un unico registro filtrando por una serie de campo, en este caso id
    # Y con get_object_or_404 es lo mismo que un get normal pero permite mostrar la pagina de 404
    category = get_object_or_404(Category,id=category_id)
    return render(request, "blog/category.html", {'category':category})

