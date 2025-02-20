from core.models import Livros
from core.serializers import LivrosSerializer
from rest_framework.viewsets import ModelViewSet

class LivrosViewSet(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer
