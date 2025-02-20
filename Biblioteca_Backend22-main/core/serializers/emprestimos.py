from core.models import Emprestimos
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response
from rest_framework import status

class EmprestimosSerializer(ModelSerializer):
    class Meta:
        model = Emprestimos
        fields = '__all__'

    def validate(self, attrs):
        if Emprestimos.objects.filter(attrs['aluno']).exists():
            return Response(data={'esse aluno ja possui livro cadastrado'}, status=status.HTTP_400_BAD_REQUEST)
        elif Emprestimos.objects.filter(attrs['livro']).exists():
            return Response(data={'esse livro ja foi pego'}, status=status.HTTP_400_BAD_REQUEST)
        return attrs