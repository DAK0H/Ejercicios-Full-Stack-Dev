#Crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. 
# Para ello, tendréis que acceder dos veces al archivo creado.

f = open("archivo.txt", "w")
f.write("Mi nombre es Pedro")
f.close()