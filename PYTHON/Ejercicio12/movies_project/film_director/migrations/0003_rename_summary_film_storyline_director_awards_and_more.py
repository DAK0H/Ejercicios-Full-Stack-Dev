# Generated by Django 4.1.6 on 2023-06-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_director', '0002_remove_director_death_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='summary',
            new_name='storyline',
        ),
        migrations.AddField(
            model_name='director',
            name='awards',
            field=models.CharField(default='Sin premios', max_length=100),
        ),
        migrations.AddField(
            model_name='director',
            name='birth_location',
            field=models.CharField(default='Sin datos', max_length=100),
        ),
        migrations.AddField(
            model_name='director',
            name='facets',
            field=models.CharField(default='Director', max_length=100),
        ),
        migrations.AddField(
            model_name='director',
            name='image_url',
            field=models.URLField(default='movies_project/static/images/no_image.png'),
        ),
        migrations.AddField(
            model_name='film',
            name='stars',
            field=models.CharField(default='Sin datos', max_length=100),
        ),
        migrations.AlterField(
            model_name='director',
            name='birth_date',
            field=models.DateField(default='Sin datos'),
        ),
        migrations.AlterField(
            model_name='film',
            name='creation_year',
            field=models.CharField(default='0000', max_length=4),
        ),
    ]