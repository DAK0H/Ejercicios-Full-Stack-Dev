# Generated by Django 4.1.6 on 2023-06-15 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_director', '0007_film_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='film',
            name='image_url',
        ),
        migrations.AddField(
            model_name='director',
            name='image',
            field=models.ImageField(default='images_movies_project/no_image.png', upload_to='media/img_directors'),
        ),
        migrations.AddField(
            model_name='film',
            name='cover',
            field=models.ImageField(default='images_movies_project/no_image.png', upload_to='media/img_films'),
        ),
    ]
