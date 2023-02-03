import sqlite3



def main():

    identifier = input('Introduce el id: ')
    name = input('Introduce el nombre: ')
    surname = input('Introduce el apellido: ')

    create_student(identifier, name, surname)


def create_student(identifier, name, surname):

    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    row = cursor.execute(f"INSERT INTO Alumnos VALUES('{identifier}', '{name}', '{surname}')")

    conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()