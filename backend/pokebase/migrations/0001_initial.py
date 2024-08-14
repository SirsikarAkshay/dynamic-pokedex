# Generated by Django 5.1 on 2024-08-14 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokedex',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('japanese_name', models.CharField(max_length=50)),
                ('pokedex_number', models.IntegerField(primary_key=True, serialize=False)),
                ('percentage_male', models.IntegerField(null=True)),
                ('type1', models.CharField(max_length=50)),
                ('type2', models.CharField(max_length=50)),
                ('classfication', models.CharField(max_length=50)),
                ('height_m', models.IntegerField(null=True)),
                ('weight_kg', models.IntegerField(null=True)),
                ('base_egg_steps', models.IntegerField(null=True)),
                ('abilities', models.TextField(null=True)),
                ('experience_growth', models.IntegerField(null=True)),
                ('base_happiness', models.IntegerField(null=True)),
                ('hp', models.IntegerField(null=True)),
                ('attack', models.IntegerField(null=True)),
                ('defense', models.IntegerField(null=True)),
                ('sp_attack', models.IntegerField(null=True)),
                ('sp_defense', models.IntegerField(null=True)),
                ('speed', models.IntegerField(null=True)),
                ('generation', models.IntegerField(null=True)),
                ('is_legendary', models.BooleanField(default=False)),
            ],
        ),
    ]
