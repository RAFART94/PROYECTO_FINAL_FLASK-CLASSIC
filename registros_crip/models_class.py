import sqlite3
import requests
from config import *
from registros_crip.models import *
from registros_crip.conexion import Conexion
from registros_crip.forms import MovementsForm


class ModelError(Exception):
    pass

class CryptoExchange():
    def __init__(self, moneda_from, moneda_to):
        self.moneda_from = moneda_from
        self.moneda_to = moneda_to
        self.rate = 0
    
    def getRate(self, APIKEY):
        url = f'https://rest.coinapi.io/v1/exchangerate/{self.moneda_from}/{self.moneda_to}?apikey={APIKEY}'
        r = requests.get(url)
        lista_monedas = r.json()
        if r.status_code == 200:
            self.rate = lista_monedas['rate']
    
            return self.rate
        else:
            raise ModelError(f'status: {self.r.status_code} error: {self.lista_monedas}')
