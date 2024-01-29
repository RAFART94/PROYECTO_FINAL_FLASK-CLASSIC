import sqlite3

def select_all():
    conexion = sqlite3.connect("data/movements.sqlite")
    cur = conexion.cursor()
    res = cur.execute('select * from Criptomovimientos;')
    filas = res.fetchall()#Los datos de columnas (2024-01-01,14:55:37,EUR,etc)
    columnas = res.description#Los nombres de columnas(id,0000)(date,0000)

    lista_diccionario= []
    diccionario = {}
    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion += 1
        
        lista_diccionario.append(diccionario)

    return lista_diccionario