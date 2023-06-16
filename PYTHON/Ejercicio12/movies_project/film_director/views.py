from django.shortcuts import render
from .models import Director, Film



def index(request, letter=None):
    if letter != None:
        directors = Director.objects.filter(name__istartswith=letter)
    else:
        directors = Director.objects.filter(name__contains=request.GET.get('search', ''))
    
    context = {
        'directors': directors
    }
    
    return render(request, 'film_director/directors_list.html', context)


def director_detail(request, id):
    director = Director.objects.get(id=id)
    films = Film.objects.filter(director_id=director)
    context = {
        'director': director,
        'films': films
    }

    return render(request, 'film_director/director_detail.html', context)


def film_detail(request, id):
    film = Film.objects.get(id=id)
    context = {
        'film': film
    }

    return render(request, 'film_director/film_detail.html', context)
