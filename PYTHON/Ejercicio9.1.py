'''Crea un script que le pida al usuario una lista de países (separados por comas). 
Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.'''

def country_list():

    country_list = input("Introduce una lista de paises separados por comas: ")
    country_list = country_list.title()    
    country_list = country_list.split(",")
    country_list = set(country_list)
    country_list = list(country_list)
    country_list.sort()
    for i in range(len(country_list)):
        country_list[i] = country_list[i].strip()
    print(country_list)

country_list()
