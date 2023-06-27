from django.db import models
from Autores.models import Autor

# Create your models here.

class Livro (models.Model):
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    paginas = models.IntegerField()
    editora = models.CharField(max_length=50)
    edicao = models.IntegerField()
    ano_publicacao = models.IntegerField()
    idioma = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.titulo
