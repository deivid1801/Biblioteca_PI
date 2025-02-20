from core.models import Alunos
from rest_framework.serializers import ModelSerializer

class AlunosSerializer(ModelSerializer):
    class Meta:
        model = Alunos
        fields = '__all__'