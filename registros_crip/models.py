import sqlite3
import pytest
from config import APIKEY
from registros_crip import models_class



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
        conexion.close()

    return lista_diccionario

def insert(registroForm):
    conexion = sqlite3.connect("data/movements.sqlite")
    cur = conexion.cursor()
    res = cur.execute('insert into Criptomovimientos ( moneda_from, cantidad_from, moneda_to, cantidad_to,precio_unitario) VALUES (?,?,?,?,?);', registroForm)

    conexion.commit()
    conexion.close()

 
def updateExchange(apikey):
    url = f'https://rest.coinapi.io/v1/exchangerate/{base}/{quota}?time={time}&apikey={APIKEY}'
    r = requests.get(url)
    respuesta = r.json()
    if r.status_code == 200:
        rate = respuesta['rate']
        time = respuesta['time']
    else:
        raise ModelError(f"status:{r.status_code}, error: {respuesta['error']}")

'''
def precio_unitario():
    conexion = sqlite3.connect("data/movements.sqlite")
    cur = conexion.cursor()
    res = cur.execute('insert into Criptomovimientos (moneda_from, cantidad_from, moneda_to, cantidad_to) VALUES (?,?,?,?,?);', registroForm)
'''


    