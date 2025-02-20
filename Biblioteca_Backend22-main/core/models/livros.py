from django.db import models

class Livros(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    data_publicacao = models.DateField()

    def __str__(self):
        return self.titulo
