from django.db import models

"""
name: The English name of the Pokemon
japanese_name: The Original Japanese name of the Pokemon
pokedex_number: The entry number of the Pokemon in the National Pokedex
percentage_male: The percentage of the species that are male. Blank if the Pokemon is genderless.
type1: The Primary Type of the Pokemon
type2: The Secondary Type of the Pokemon
classification: The Classification of the Pokemon as described by the Sun and Moon Pokedex
height_m: Height of the Pokemon in metres
weight_kg: The Weight of the Pokemon in kilograms
capture_rate: Capture Rate of the Pokemon
base_egg_steps: The number of steps required to hatch an egg of the Pokemon
abilities: A stringified list of abilities that the Pokemon is capable of having
experience_growth: The Experience Growth of the Pokemon
base_happiness: Base Happiness of the Pokemon
against_?: Eighteen features that denote the amount of damage taken against an attack of a particular type
hp: The Base HP of the Pokemon
attack: The Base Attack of the Pokemon
defense: The Base Defense of the Pokemon
sp_attack: The Base Special Attack of the Pokemon
sp_defense: The Base Special Defense of the Pokemon
speed: The Base Speed of the Pokemon
generation: The numbered generation which the Pokemon was first introduced
is_legendary: Denotes if the Pokemon is legendary.
"""

# Create your models here.
class Pokedex(models.Model):
    name = models.CharField(max_length=50)
    japanese_name = models.CharField(max_length=50)
    pokedex_number = models.IntegerField(primary_key=True)
    percentage_male = models.IntegerField(null=True)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50)
    classfication = models.CharField(max_length=50)
    height_m = models.IntegerField(null=True)
    weight_kg = models.IntegerField(null=True)
    base_egg_steps = models.IntegerField(null=True)
    abilities = models.TextField(null=True)
    experience_growth = models.IntegerField(null=True)
    base_happiness = models.IntegerField(null=True)
    hp = models.IntegerField(null=True)
    attack = models.IntegerField(null=True)
    defense = models.IntegerField(null=True)
    sp_attack = models.IntegerField(null=True)
    sp_defense = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    generation = models.IntegerField(null=True)
    is_legendary = models.BooleanField(default=False)

    def __str__(self):
        return self.name


