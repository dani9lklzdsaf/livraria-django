from rest_framework import viewsets
from .models import Livro
from .serializers import LivroSerializer
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework import permissions

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [HasAPIKey | permissions.IsAuthenticated]
