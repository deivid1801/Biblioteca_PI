from django.db import models

class Alunos(models.Model):
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField()
    CURSO_CHOICES = [
        ('informatica', 'Informatica Para Internet'),
        ('quimica', 'Quimica'),
        ('agropecuaria', 'Agropecuaria'),
    ]
    curso = models.CharField(max_length=20, choices=CURSO_CHOICES)

    def __str__(self):
        return f'{self.nome} - {self.matricula}'


