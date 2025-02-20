from django.db import models
from core.models import Livros, Alunos
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_book(id):
        if Emprestimos.objects.filter(livro=id).exists():
            raise ValidationError(_("Esse livro já foi pego."))
        return None
        
        
def validate_studant(id):
    if Emprestimos.objects.filter(aluno=id).exists():
        raise ValidationError(_("Esse aluno já tem um empréstimo ativo."))
    return None
        
class Emprestimos(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE, validators=[validate_studant] )
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE, validators=[validate_book] )
    data_emprestimo = models.DateField(auto_now=True)
    date_devolucao = models.DateField()

    def __str__(self):
          return f'{self.aluno.nome} - {self.livro.titulo} - {self.date_devolucao}'

    
    

    





