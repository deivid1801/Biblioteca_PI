from rest_framework.viewsets import ModelViewSet
from core.serializers import AlunosSerializer
from core.models import Alunos

class AlunosViewSet(ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunosSerializer