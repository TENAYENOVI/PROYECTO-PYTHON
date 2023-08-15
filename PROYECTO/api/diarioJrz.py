import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

conn = sqlite3.connect("diarioJrz.db")

#crea un cursor para interactuar con la base de datos
cursor = conn.cursor()


#Crea la tabla usuaruis de 3 columnas
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Notas (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               lugar TEXT NOT NULL,
               noticia TEXT NOT NULL
               )''')

#Guarda los cambios y cierra la conexion
conn.commit()
conn.close()


class Noticias(BaseModel):
    id: int
    titulo: str
    lugar: str
    noticia: str

app = FastAPI() 

@app.post("/agregar/")
async def agregarDatos(datos: Noticias):
    conn = sqlite3.connect("diarioJrz.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Notas (titulo,lugar,noticia) VALUES (?,?,?)", (datos.titulo,datos.lugar,datos.noticia))
    conn.commit()
    conn.close()
    return {"message": "Registro capturado correctamente!!!"}

@app.get("/datos/")
async def leerDatos():
    conn = sqlite3.connect("diarioJrz.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Notas")
    resultados = cursor.fetchall()
    conn.close()
    if resultados:
        return[{"id":resultado[0],"titulo": resultado[1],"lugar":resultado[2],"noticia": resultado[3]} for resultado in resultados]
    else:
        return {"message":"Base de datos vacia"}


@app.get("/getdatos/{id}/")
async def NotabyId(id:int):
    conn = sqlite3.connect("diarioJrz.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Notas WHERE id=?",(id,))
    resultado = cursor.fetchone()
    conn.close()
    if resultado is not None:
        return{"titulo": resultado[0],"lugar":resultado[1],"noticia": resultado[2]}
    else:
        return {"message":"Id no encontrado"}


@app.put("/actualizar/{id}/")
async def actualizarDatos(id:int, datos: Noticias):
    conn = sqlite3.connect("diarioJrz.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Notas set titulo=?, lugar=?, noticia=? WHERE id=?",(datos.titulo,datos.lugar,datos.noticia,id))
    conn.commit()
    conn.close()
    return {"message": "Registro actualizado correctamente!!!"}

@app.delete("/eliminar/{id}")
async def eliminarDatos(id: int):
    conn = sqlite3.connect("diarioJrz.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Notas WHERE id=?",(id,))
    conn.commit()
    conn.close()
    return {"message": "Registro eliminado correctamente!!!"}



conn = sqlite3.connect("diarioJrz.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO Notas (titulo,lugar,noticia) VALUES (?,?,?)",("Cae rendida de cansancio","Casa","trabajo sin parar y al llegar a casa se durmio"))

conn.commit()
conn.close()