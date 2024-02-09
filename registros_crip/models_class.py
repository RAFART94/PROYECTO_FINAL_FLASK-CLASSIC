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
            raise ModelError(f'status: {r.status_code} error: {lista_monedas["error"]}')

class CryptoSuma():
    def __init__(self):
        pass

    def criptoToSuma(self):#Recibe la suma de todas las criptos compradas en la base de datos y se suma a los totales de criptomonedas
        conexion = Conexion('select sum(cantidad_to), moneda_to from Criptomovimientos group by moneda_to')
        suma = conexion.res.fetchall()
        if suma != '':
            total_criptos_to = []
            for s in suma:
                if s[1] != 'EUR':
                    total_criptos_to.append(s)
            conexion.con.close()

            return total_criptos_to
        else:
            return 0
        
    def criptoFromSuma(self):#Recibe la suma de todas las critpos gastadas en la base de datos y se suma a los totales gastados en criptomonedas
        conexion = Conexion('select sum(cantidad_from), moneda_from from Criptomovimientos group by moneda_from')
        suma = conexion.res.fetchall()
        if suma != '':
            total_criptos_from = []
            for s in suma:
                if s[1] != 'EUR':
                    total_criptos_from.append(s)
            conexion.con.close()

            return total_criptos_from
        else:
            return 0

    def criptoResta(self):#Total de criptos compradas menos total de criptos gastadas
        cripto_to = self.criptoToSuma()
        cripto_from = self.criptoFromSuma()
        resultado = []
        if cripto_to != 0 and cripto_from != 0:
            for suma_to in cripto_to:
                for suma_from in cripto_from:
                    if suma_to[1] == suma_from[1]:
                        resta = suma_to[0] - suma_from[0]
                        resultado.append(suma_from[1])
                        resultado.append(resta)
                        nuevo_resultado = [(resultado[i], resultado[i+1]) for i in range(0, len(resultado), 2)]
                        resultado = nuevo_resultado
                        return resultado
        else:
            return 0
        
    def rateMyCripto(self):
        resta_cripto = self.criptoResta()
        lista_valores_cripto = []
        if resta_cripto != None:
            for c in resta_cripto:
                cripto = c[0]
                r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{cripto}/EUR?apikey={APIKEY}')
                resultado = r.json()
                if r.status_code == 200:
                    rate = resultado['rate']
                    valor_cripto = rate * c[1]
                    lista_valores_cripto.append(valor_cripto)
                else:
                    raise ModelError(f'status: {r.status_code} error: {resultado["error"]}')
            
            return sum(lista_valores_cripto)
        else:
            return 0


