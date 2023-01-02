#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
'''Un año dado es bisiesto si es divisible entre cuatro y (no es divisible entre 100 o es divisible entre 400)'''

def leap_year():
    year = int(input('¿Qué año quieres comprobar si es bisiesto?'))
    if year %4 == 0 and (year %100 != 0 or year %400 == 0):
        print(year, 'es un año bisiesto')
    else:
        print(year, 'no es un año bisiesto')
leap_year()