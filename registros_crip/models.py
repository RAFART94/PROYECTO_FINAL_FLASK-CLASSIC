import requests
from registros_crip.models_class import *
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

def save(registroForm):
    conexion = Conexion('insert into Criptomovimientos (date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, precio_unitario) VALUES (?,?,?,?,?,?,?);', registroForm)
    conexion.con.commit()
    conexion.con.close()

def euros_gastados():
    conexion = Conexion('select sum(cantidad_from) from Criptomovimientos where moneda_from = "EUR"')
    resultado = conexion.res.fetchall()
    conexion.con.close()
    if resultado[0][0] is None:
        resultado = 0
    else:
        resultado = f'{resultado[0][0]:,.2f}'
        resultado = resultado.replace(',', '*')
        resultado = resultado.replace('.', ',')
        resultado = resultado.replace('*', '.')
    return resultado

def euros_gastados_bruto():
    conexion = Conexion('select sum(cantidad_from) from Criptomovimientos where moneda_from = "EUR"')
    resultado = conexion.res.fetchall()
    conexion.con.close()
    if resultado [0][0] is None:
        resultado = 0
    else:
        resultado = resultado[0][0]
    return resultado

def euros_ganados():
    conexion = Conexion('select sum(cantidad_to) from Criptomovimientos where moneda_to = "EUR"')
    resultado = conexion.res.fetchall()
    conexion.con.close()
    if resultado[0][0] is None:
        resultado = 0
    else:
        resultado = f'{resultado[0][0]:,.2f}'
        resultado = resultado.replace(',', '*')
        resultado = resultado.replace('.', ',')
        resultado = resultado.replace('*', '.')
    return resultado

def euros_ganados_bruto():
    conexion = Conexion('select sum(cantidad_to) from Criptomovimientos where moneda_to = "EUR"')
    resultado = conexion.res.fetchall()
    conexion.con.close()
    if resultado [0][0] is None:
        resultado = 0
    else:
        resultado = resultado[0][0]
    return resultado

def cripto_individual_ganada(cripto):
    conexion = Conexion(f'select sum(cantidad_to) from Criptomovimientos where moneda_to = "{cripto}"')
    resultado = conexion.res.fetchall()
    conexion.con.close()
    if resultado [0][0] is None:
        resultado = 0
    else:
        resultado = resultado[0][0]
    return resultado

def formato_cantidad(cantidad):
    if cantidad >= 1:
        resultado = f'{cantidad:,.2f}'
        resultado = resultado.replace(',', '*')
        resultado = resultado.replace('.', ',')
        resultado = resultado.replace('*', '.')
    elif cantidad == 0:
        resultado = 0
    elif cantidad < 0:
        resultado = f'{cantidad:,.2f}'
        resultado = resultado.replace(',', '*')
        resultado = resultado.replace('.', ',')
        resultado = resultado.replace('*', '.')
    else:
        resultado = f'{cantidad:,.6f}'
        resultado = resultado.replace(',', '*')
        resultado = resultado.replace('.', ',')
        resultado = resultado.replace('*', '.')

    return resultado

def mostrar_monedas_to():
    conexion = Conexion(f'select moneda_to from Criptomovimientos')
    resultado = conexion.res.fetchall()
    conexion.con.close()
    lista = []
    for moneda in resultado:
        lista.append(moneda[0])
    return lista

def cripto_from(cripto):
    conexion = Conexion(f'select sum(cantidad_from) from Criptomovimientos where moneda_from = "{cripto}"')
    resultado = conexion.res.fetchall()
    conexion.con.close()
    if resultado[0][0] is None:
        resultado = 0
    else:
        resultado = resultado[0][0]
    return resultado