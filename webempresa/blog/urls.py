from django.urls import path
from . import views as views

urlpatterns = [
    # Paths del url
    path('', views.posts, name='blog'),
    path('category/<int:category_id>/', views.category, name='category'),
]
