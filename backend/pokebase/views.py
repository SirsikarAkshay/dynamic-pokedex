from django.shortcuts import render
from .models import Pokedex
from rest_framework import generics
from pokebase.serializers import PokedexSerializer

# Create your views here.

#List or create API views
class PokedexListCreate(generics.ListCreateAPIView):
    queryset = Pokedex.objects.all()
    serializer_class = PokedexSerializer

#Retrieve, Update or delete a specific view
class PokedexRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pokedex.objects.all()
    serializer_class = PokedexSerializer

#Filter the model by name of the author
class PokedexByName(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned pokemon to given names.,
        by filtering against a 'name' query parameter in the URL.
        """
        queryset = Pokedex.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset

class PokedexByHP(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        hp_lower = self.request.query_params.get('hp_lower', None)
        hp_upper = self.request.query_params.get('hp_upper', None)
        hp_equal = self.request.query_params.get('hp_equal', None)

        if hp_lower is not None:
            queryset = queryset.filter(hp__lt=hp_lower)
        if hp_upper is not None:
            queryset = queryset.filter(hp__gt=hp_upper)
        if hp_equal is not None:
            queryset = queryset.filter(hp=hp_equal)

        return queryset

class PokedexByHeight(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        height_lower = self.request.query_params.get('height_lower', None)
        height_upper = self.request.query_params.get('height_upper', None)
        height_equal = self.request.query_params.get('height_equal', None)

        if height_lower is not None:
            queryset = queryset.filter(height_m__lt=height_lower)
        if height_upper is not None:
            queryset = queryset.filter(height_m__gt=height_upper)
        if height_equal is not None:
            queryset = queryset.filter(height_m=height_equal)

        return queryset

class PokedexByWeight(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        weight_lower = self.request.query_params.get('weight_lower', None)
        weight_upper = self.request.query_params.get('weight_upper', None)
        weight_equal = self.request.query_params.get('weight_equal', None)

        if weight_lower is not None:
            queryset = queryset.filter(weight_kg__lt=weight_lower)
        if weight_upper is not None:
            queryset = queryset.filter(weight_kg__gt=weight_upper)
        if weight_equal is not None:
            queryset = queryset.filter(weight_kg=weight_equal)

        return queryset

class PokedexByPercentMale(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        percentage_male_lower = self.request.query_params.get('percentage_male_lower', None)
        percentage_male_upper = self.request.query_params.get('percentage_male_upper', None)
        percentage_male_equal = self.request.query_params.get('percentage_male_equal', None)

        if percentage_male_lower is not None:
            queryset = queryset.filter(percentage_male__lt=percentage_male_lower)
        if percentage_male_upper is not None:
            queryset = queryset.filter(percentage_male__gt=percentage_male_upper)
        if percentage_male_equal is not None:
            queryset = queryset.filter(percentage_male=percentage_male_equal)

        return queryset

class PokedexByBaseEggSteps(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        base_egg_steps_lower = self.request.query_params.get('base_egg_steps_lower', None)
        base_egg_steps_upper = self.request.query_params.get('base_egg_steps_upper', None)
        base_egg_steps_equal = self.request.query_params.get('base_egg_steps_equal', None)

        if base_egg_steps_lower is not None:
            queryset = queryset.filter(base_egg_steps__lt=base_egg_steps_lower)
        if base_egg_steps_upper is not None:
            queryset = queryset.filter(base_egg_steps__gt=base_egg_steps_upper)
        if base_egg_steps_equal is not None:
            queryset = queryset.filter(base_egg_steps=base_egg_steps_equal)

        return queryset

class PokedexByExperienceGrowth(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        experience_growth_lower = self.request.query_params.get('experience_growth_lower', None)
        experience_growth_upper = self.request.query_params.get('experience_growth_upper', None)
        experience_growth_equal = self.request.query_params.get('experience_growth_equal', None)

        if experience_growth_lower is not None:
            queryset = queryset.filter(experience_growth__lt=experience_growth_lower)
        if experience_growth_upper is not None:
            queryset = queryset.filter(experience_growth__gt=experience_growth_upper)
        if experience_growth_equal is not None:
            queryset = queryset.filter(experience_growth=experience_growth_equal)

        return queryset

class PokedexByBaseHappiness(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        base_happiness_lower = self.request.query_params.get('base_happiness_lower', None)
        base_happiness_upper = self.request.query_params.get('base_happiness_upper', None)
        base_happiness_equal = self.request.query_params.get('base_happiness_equal', None)

        if base_happiness_lower is not None:
            queryset = queryset.filter(base_happiness__lt=base_happiness_lower)
        if base_happiness_upper is not None:
            queryset = queryset.filter(base_happiness__gt=base_happiness_upper)
        if base_happiness_equal is not None:
            queryset = queryset.filter(base_happiness=base_happiness_equal)

        return queryset

class PokedexByAttack(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        attack_lower = self.request.query_params.get('attack_lower', None)
        attack_upper = self.request.query_params.get('attack_upper', None)
        attack_equal = self.request.query_params.get('attack_equal', None)

        if attack_lower is not None:
            queryset = queryset.filter(attack__lt=attack_lower)
        if attack_upper is not None:
            queryset = queryset.filter(attack__gt=attack_upper)
        if attack_equal is not None:
            queryset = queryset.filter(attack=attack_equal)

        return queryset

class PokedexByDefense(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        defense_lower = self.request.query_params.get('defense_lower', None)
        defense_upper = self.request.query_params.get('defense_upper', None)
        defense_equal = self.request.query_params.get('defense_equal', None)

        if defense_lower is not None:
            queryset = queryset.filter(defense__lt=defense_lower)
        if defense_upper is not None:
            queryset = queryset.filter(defense__gt=defense_upper)
        if defense_equal is not None:
            queryset = queryset.filter(defense=defense_equal)

        return queryset

class PokedexBySpAttack(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        sp_attack_lower = self.request.query_params.get('sp_attack_lower', None)
        sp_attack_upper = self.request.query_params.get('sp_attack_upper', None)
        sp_attack_equal = self.request.query_params.get('sp_attack_equal', None)

        if sp_attack_lower is not None:
            queryset = queryset.filter(sp_attack__lt=sp_attack_lower)
        if sp_attack_upper is not None:
            queryset = queryset.filter(sp_attack__gt=sp_attack_upper)
        if sp_attack_equal is not None:
            queryset = queryset.filter(sp_attack=sp_attack_equal)

        return queryset


class PokedexBySpDefense(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        sp_defense_lower = self.request.query_params.get('sp_defense_lower', None)
        sp_defense_upper = self.request.query_params.get('sp_defense_upper', None)
        sp_defense_equal = self.request.query_params.get('sp_defense_equal', None)

        if sp_defense_lower is not None:
            queryset = queryset.filter(sp_defense__lt=sp_defense_lower)
        if sp_defense_upper is not None:
            queryset = queryset.filter(sp_defense__gt=sp_defense_upper)
        if sp_defense_equal is not None:
            queryset = queryset.filter(sp_defense=sp_defense_equal)

        return queryset

class PokedexBySpeed(generics.ListAPIView):
    serializer_class = PokedexSerializer

    def get_queryset(self):
        queryset = Pokedex.objects.all()
        speed_lower = self.request.query_params.get('speed_lower', None)
        speed_upper = self.request.query_params.get('speed_upper', None)
        speed_equal = self.request.query_params.get('speed_equal', None)

        if speed_lower is not None:
            queryset = queryset.filter(speed__lt=speed_lower)
        if speed_upper is not None:
            queryset = queryset.filter(speed__gt=speed_upper)
        if speed_equal is not None:
            queryset = queryset.filter(speed=speed_equal)

        return queryset


