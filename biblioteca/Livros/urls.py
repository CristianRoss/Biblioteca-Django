from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('livro/<int:livro_id>', views.livro, name='livro'),
]