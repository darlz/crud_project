from .models import Proyect
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProyectViewSet(viewsets.ModelViewSet):
    queryset = Proyect.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer