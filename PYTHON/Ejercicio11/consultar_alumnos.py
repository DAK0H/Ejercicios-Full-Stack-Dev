import sqlite3

def main():

    name = input('Introduce el nombre: ')
    search_student(name)

def search_student(name):
    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    rows = cursor.execute(f"SELECT * FROM Alumnos WHERE nombre = '{name}'")

    print('Este alumno/a no está en la base de datos.' if rows.fetchone() == None else cursor.fetchall())
    
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()