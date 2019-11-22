from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import SnippetSerializer, UserSnippetSerializer
from .models import Snippet
from scriptmanager.permissions import IsOwnerOrReadOnly

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'scriptmanager/index.html')


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSnippetSerializer
    permission_classes = [permissions.IsAdminUser]
    def perform_create(self, serializer):
        serializer.save()


class SnippetView(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    def perform_create(self, serializer):  
        serializer.save(owner=self.request.user)