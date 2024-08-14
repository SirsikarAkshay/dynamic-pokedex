from .models import Pokedex
from rest_framework import serializers

class PokedexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokedex
        fields = '__all__'
        depth = 1
