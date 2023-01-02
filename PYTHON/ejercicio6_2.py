'''En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno 
que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.'''

class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def print_data(self):
        print(f'Nombre del alumno/a: {self.name}')
        print(f'Nota: {self.grade}')
    
    def result(self):
        if self.grade >= 5:
            print(f'{self.name} ha aprobado')
        else:
            print(f'{self.name} ha suspendido') 
    
student = Student('Alicia', 7)
student.print_data()
student.result()