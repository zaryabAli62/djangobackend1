from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'content', 'created_at']  # Keep the user field but make it read-only
        read_only_fields = [ 'created_at'] 
 
