#Crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, 
# lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehiculo:
    def __init__(self, marca, modelo, color, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.cilindrada = cilindrada

    def __str__(self):
        return 'Marca: ' + self.marca + '\nModelo: ' + self.modelo + '\nColor: ' + self.color + '\nCilindrada: ' + self.cilindrada

v1 = Vehiculo('Seat', 'Leon', 'Rojo', '1.4')
f = open('vehiculo.txt', 'wb')
pickle.dump(v1, f)
f.close()

f = open('vehiculo.txt', 'rb')
v2 = pickle.load(f)
f.close()
print(v2)