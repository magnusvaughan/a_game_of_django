from rest_framework import serializers
from .models import Character


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ('id', 'name', 'is_female', 'culture', 
        'aliases', 'born', 'died', 'father', 'mother', 'spouse', 
        'children', 'allegiances', 'books', 'pov_books', 'played_by', 
        'tv_series')