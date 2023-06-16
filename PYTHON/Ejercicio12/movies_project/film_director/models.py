from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    birth_date = models.DateField(blank=False, null=False)
    birth_location = models.CharField(max_length=100, blank=False, null=False)
    age = models.CharField(default='Edad', max_length=4)
    facets = models.CharField(default='Director', max_length=100)
    awards = models.CharField(default='Sin premios', max_length=100)
    image = models.ImageField(default='images_movies_project/no_image.png',
                              upload_to='media/img_directors')

    def __str__(self):
        return f'{self.name} {self.last_name}'


class Film(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    creation_year = models.CharField(max_length=4, blank=False, null=False)
    duration = models.CharField(default='0h', max_length=10, blank=False, 
                                null=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    main_actors = models.CharField(max_length=100, blank=False, null=False)
    storyline = models.TextField(blank=False, null=False)
    cover = models.ImageField(default='images_movies_project/no_image.png',
                              upload_to='media/img_films')

    def __str__(self):
        return self.title
