from core.models import Emprestimos
from core.serializers import EmprestimosSerializer
from rest_framework.viewsets import ModelViewSet

class EmprestimosViewSet(ModelViewSet):
    queryset = Emprestimos.objects.all()
    serializer_class = EmprestimosSerializer
