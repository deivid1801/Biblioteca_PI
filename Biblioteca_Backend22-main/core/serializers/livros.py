from core.models import Livros
from rest_framework.serializers import ModelSerializer

class LivrosSerializer(ModelSerializer):
    class Meta:
        model = Livros
        fields = '__all__'

