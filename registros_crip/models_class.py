from registros_crip import models
from config import APIKEY

class ModelError(Exception):
    pass

class AllCoinsApiIO():
    def __init__(self):
        self.url = ''
        self.asset_id = ['EUR', 'ETH', 'BNB', 'ADA', 'DOT',
                         'BTC', 'USDT', 'XRP', 'SOL', 'MATIC']
        self.lista_no_criptos = []
        self.lista_criptos = []
        self.lista_general = []
        
    def getMyCoins(self, base, quota, apikey):
        url = f'https://rest.coinapi.io/v1/assets/?apikey={apikey}'
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception('Error en consulta condigo:{}'.format(r.status_code))
        
        self.lista_general = r.json()

        for dic in self.lista_general:
            if dic["asset_id"] == 'EUR':
                self.lista_no_criptos.append(dic["asset_id"])
            else:
                self.lista_criptos.append(dic['asset_id'])
    
class Exchange():
    def __init__(self, base, quota, time):
        self.rate = None
        self.moneda_base = base
        self.moneda_quota = quota
        self.status_code = None
        self.time = time
        self.moneda_no_cripto = None

    def updateExchange(self, base, quota, time, apikey):
        url = f'https://rest.coinapi.io/v1/exchangerate/{base}/{quota}?time={time}&apikey={apikey}'
        r = requests.get(url)
        self.status_code = r.status_code
        respuesta = r.json()
        if r.status_code == 200:
            self.rate = respuesta['rate']
            self.time = respuesta['time']
        else:
            raise ModelError(f"status:{r.status_code}, error: {respuesta['error']}")
    