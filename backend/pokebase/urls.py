from django.urls import path
from .views import (PokedexRetrieveUpdateDestroy, PokedexListCreate, PokedexByName, PokedexByHP,
                    PokedexByHeight, PokedexByWeight, PokedexByPercentMale, PokedexByBaseEggSteps,
                    PokedexByExperienceGrowth, PokedexByBaseHappiness, PokedexByAttack, PokedexByDefense,
                    PokedexBySpAttack, PokedexBySpDefense, PokedexBySpeed)

urlpatterns = [
    path('pokemon/', PokedexListCreate.as_view(), name='pokedex-list'),
    path('pokemon/<int:pk>/', PokedexRetrieveUpdateDestroy.as_view(), name='pokedex-detail'),
    path('pokemon/name/', PokedexByName.as_view(), name='pokedex-by-name'),
    path('pokemon/hp/', PokedexByHP.as_view(), name='pokedex-by-hp'),
    path('pokemon/height/', PokedexByHeight.as_view(), name='pokedex-by-height'),
    path('pokemon/weight/', PokedexByWeight.as_view(), name='pokedex-by-weight'),
    path('pokemon/male/', PokedexByPercentMale.as_view(), name='pokedex-by-male'),
    path('pokemon/egg/', PokedexByBaseEggSteps.as_view(), name='pokedex-by-egg'),
    path('pokemon/experience/', PokedexByExperienceGrowth.as_view(), name='pokedex-by-exp'),
    path('pokemon/happiness/', PokedexByBaseHappiness.as_view(), name='pokedex-by-happiness'),
    path('pokemon/attack/', PokedexByAttack.as_view(), name='pokedex-by-attack'),
    path('pokemon/defense/', PokedexByDefense.as_view(), name='pokedex-by-defense'),
    path('pokemon/sp_attack/', PokedexBySpAttack.as_view(), name='pokedex-by-sp-attack'),
    path('pokemon/sp_defense/', PokedexBySpDefense.as_view(), name='pokedex-by-sp-defense'),
    path('pokemon/speed/', PokedexBySpeed.as_view(), name='pokedex-by-speed'),
]
