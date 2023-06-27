from django.contrib import admin
from .models import Livro
from .models import Autor


# Register your models here.

class ExibeLivro(admin.ModelAdmin):
 list_display = ('id', 'titulo', 'ano_publicacao', 'isbn')
 list_display_links = ('id', 'titulo')
 search_fields = ('titulo',)
 list_filter = ('ano_publicacao',)
 list_per_page = 2

admin.site.register(Livro, ExibeLivro)

class ExibeAutor(admin.ModelAdmin):
 list_display = ('id', 'nome', 'nacionalidade')
 list_display_links = ('id', 'nome')
 search_fields = ('nome',)
 list_filter = ('nacionalidade',)
 list_per_page = 2

admin.site.register(Autor, ExibeAutor)
