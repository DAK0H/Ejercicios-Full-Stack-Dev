# Generated by Django 4.1.6 on 2023-06-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_director', '0004_rename_stars_film_main_actors_director_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image_url',
            field=models.URLField(default=''),
        ),
    ]
