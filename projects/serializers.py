from rest_framework import serializers
from .models import Proyect

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id', 'title', 'description', 'tecnology', 'created_at')
        read_only_fields = ('created_at',)