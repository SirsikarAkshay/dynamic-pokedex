import csv
from django.core.management.base import BaseCommand
from pokebase.models import Pokedex
import pandas as pd

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

class Command(BaseCommand):
    help = 'Import books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        df = pd.read_csv(csv_file)
        df = df.fillna(0)
        df['weight_kg'] = df['weight_kg'].astype(int)
        df['percentage_male'] = df['percentage_male'].astype(int)
        df['height_m'] = df['height_m'].astype(int)


        df.to_csv(csv_file, index=False)

        with open(csv_file, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Pokedex.objects.create(
                    name=row['name'],
                    japanese_name=row['japanese_name'],
                    pokedex_number=row['pokedex_number'],
                    percentage_male=row['percentage_male'],
                    type1=row['type1'],
                    type2=row['type2'],
                    classfication=row['classfication'],
                    height_m=row['height_m'],
                    weight_kg=row['weight_kg'],
                    base_egg_steps=row['base_egg_steps'],
                    abilities=row['abilities'],
                    experience_growth=row['experience_growth'],
                    base_happiness=row['base_happiness'],
                    hp=row['hp'],
                    attack=row['attack'],
                    defense=row['defense'],
                    sp_attack=row['sp_attack'],
                    sp_defense=row['sp_defense'],
                    speed=row['speed'],
                    generation=row['generation'],
                    is_legendary=row['is_legendary']
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported pokedex from CSV'))
