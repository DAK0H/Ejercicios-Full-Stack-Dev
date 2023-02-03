import sqlite3

def main():

    create_table()

def create_table():

    conn = sqlite3.connect('alumnos.db')
    cursor = conn.cursor()

    row = cursor.execute("""
    CREATE TABLE Alumnos (
        id INTEGER PRIMARY KEY, 
        nombre TEXT NOT NULL, 
        apellido TEXT NOT NULL
    );
    """)

    conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()