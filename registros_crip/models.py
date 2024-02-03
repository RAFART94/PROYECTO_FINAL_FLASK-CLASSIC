import sqlite3
import requests
from config import APIKEY
from registros_crip.conexion import Conexion
from registros_crip.forms import MovementsForm



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
    conexion = Conexion('insert into Criptomovimientos ( date, time, moneda_from, cantidad_from, moneda_to, cantidad_to, precio_unitario) VALUES (?,?,?,?,?,?,?);', registroForm)

    conexion.con.commit()
    conexion.con.close()

 
def getEUR():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'EUR':
            euro = item['asset_id']
    return euro

def getEUR():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'EUR':
            euro = item['asset_id']
    return euro

def getEUR():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'EUR':
            euro = item['asset_id']
    return euro

def getBTC():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'BTC':
            btc = item['asset_id']
    return btc

def getETH():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'ETH':
            eth = item['asset_id']
    return eth

def getUSDT():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'USDT':
            usdt = item['asset_id']
    return usdt

def getBNB():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'BNB':
            bnb = item['asset_id']
    return bnb

def getXRP():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'XRP':
            xrp = item['asset_id']
    return xrp

def getADA():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'ADA':
            ada = item['asset_id']
    return ada

def getSOL():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'SOL':
            sol = item['asset_id']
    return sol

def getDOT():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'DOT':
            dot = item['asset_id']
    return dot

def getMATIC():
    url = f'https://rest.coinapi.io/v1/assets/?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    for item in lista_monedas:
        if item['asset_id'] == 'MATIC':
            matic = item['asset_id']
    return matic

def getRate(APIKEY):
    moneda_from = MovementsForm(moneda_from)
    moneda_to = MovementsForm(moneda_to)
    url = f'https://rest.coinapi.io/v1/exchangerate/{moneda_from}/{moneda_to}?apikey={APIKEY}'
    r = requests.get(url)
    lista_monedas = r.json()
    if r.status_code == 200:
        rate = lista_monedas['rate']
    
    return rate


    