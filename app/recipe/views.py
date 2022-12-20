"""
Views for the recipe apis
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """"View for manage recipe apis"""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrive recipes for auth user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_clas(self):
        """Return serializer class for request"""
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class
