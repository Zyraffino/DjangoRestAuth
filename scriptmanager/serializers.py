from rest_framework import serializers
from .models import Snippet, Project
from django.contrib.auth.models import User

class UserSnippetSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'pub_date')

class SnippetSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = (
            'owner',
            'project',
            'file_name',
            'language',
            'style',
            'linenos',
            'snippet',
            'highlighted',
            'created_at',
        )
        read_only_fields = ('file_name','created_at',)