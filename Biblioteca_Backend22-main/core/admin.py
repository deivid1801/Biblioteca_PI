from django.contrib import admin
from .models import Alunos, Emprestimos, Livros

admin.site.register(Alunos)
admin.site.register(Emprestimos)
admin.site.register(Livros)