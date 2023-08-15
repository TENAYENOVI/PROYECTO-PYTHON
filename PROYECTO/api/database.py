import sqlite3


#Realiza una conexion a la base de datos "SI NO EXISTE", la crea
conn = sqlite3.connect("prueba.db")

#crea un cursor para interactuar con la base de datos
cursor = conn.cursor()


#Crea la tabla usuaruis de 3 columnas
cursor.execute('''
               CREATE TABLE IF NOT EXISTS USUARIOS (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               edad INTEGER
               )''')


#Guarda los cambios y cierra la conexion
conn.commit()
conn.close()

conn = sqlite3.connect("prueba.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO USUARIOS (nombre,edad) VALUES (?,?)",("Ivone",29))

conn.commit()
conn.close()