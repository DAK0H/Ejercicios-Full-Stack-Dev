'''
Crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. 
Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una 
operación para calcular el tiempo que queda de trabajo.
'''
import time

# Obtengo la fecha actual estructurada en el huso horario UTC 
time_tuple = time.gmtime()

#Utilizo variables para guardar los datos hora, min y sec de la tupla y ajusto UTC+1
hour = time_tuple[3] + 1
min = time_tuple[4]
sec = time_tuple[5]

#Paso la hora, minutos y segundos actual a segundos
actual_total_sec = (hour*60*60)+(min*60)+sec

#Guardo los segundos totales de la hora de irse a casa que son: 19horas*60*60 = 68400sec
time_home_sec = 68400

def what_time():

    if actual_total_sec >= time_home_sec:
        print(f'Son las {hour} horas y {min} minutos, ya es hora de irse a casa')

    else:       
        sec_left = time_home_sec - actual_total_sec
        print(f'Son las {hour} horas y {min} minutos')
        print(f'Faltan aún {sec_left//3600} horas, {(sec_left%3600)//60} minutos y {(sec_left%3600)%60} segundos para irse a casa')

what_time()





