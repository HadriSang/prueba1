from django.urls import path
from . import views

urlpatterns = [
    # Paths del page
    path('<int:page_id>/<slug:page_slug>', views.page, name='page'),
]
