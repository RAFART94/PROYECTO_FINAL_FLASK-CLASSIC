import sqlite3
from config import APIKEY
from registros_crip.conexion import Conexion



def select_all():
    conexion = Conexion('select id,date,time,moneda_from,cantidad_from,moneda_to,cantidad_to,precio_unitario from Criptomovimientos order by date DESC, time DESC;')
    filas = conexion.res.fetchall()
    columnas = conexion.res.description

    lista_diccionario= []

    for f in filas:
        posicion = 0
        diccionario = {}
        for c in columnas:
            diccionario[c[0]] = f[posicion]
            posicion += 1
        
        lista_diccionario.append(diccionario)
        conexion.con.close()

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


    