'''
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

    Color
    Ruedas
    Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

    Velocidad
    Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
'''
class Vehicle():
    color = 'blanco'
    wheels = 4
    doors = 5

class Car(Vehicle):
    speed = 120
    displacement = 90

car = Car()
print(f'Este coche es de color {car.color}, tiene {car.wheels} ruedas y {car.doors} puertas.') 
print(f'Su cilindrada es de {car.displacement}CV y alcanza unos {car.speed}km/h.')
