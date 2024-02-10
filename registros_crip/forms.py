from flask import Flask
from flask_wtf import FlaskForm
from wtforms import DateField,FloatField,SubmitField,TimeField,SelectField
from wtforms.validators import DataRequired,ValidationError
from config import *
from registros_crip.models import *
from registros_crip.models_class import *
from registros_crip.conexion import Conexion


MONEDAS = [('EUR', 'Euro (EUR)'), ('DOT','Polkadot (DOT)'), ("XRP", "XRP (XRP)"),
            ('BTC', 'Bitcoin (BTC)'), ('ETH', 'Ethereum (ETH)'), ('SOL','Solana (SOL)'),
            ('MATIC', 'Polygon (MATIC)'),  ('USDT', 'Tether (USDT)'), ('BNB', 'Binance Coin (BNB)'),
            ('ADA', 'Cardano (ADA)')]

def MonedasDisponibles():
    MONEDA_FROM = ['EUR']
    conexion = Conexion('select moneda_to from Criptomovimientos')
    lista_monedas = conexion.res.fetchall()
    for moneda in lista_monedas:
        if moneda != 'EUR':
            if moneda[0] == 'BTC':
                moneda[0].replace('BTC', 'Bitcoin (BTC)')
            MONEDA_FROM.append(moneda[0])
            MONEDA_FROM = list(dict.fromkeys(MONEDA_FROM))

    return MONEDA_FROM

class MovementsForm(FlaskForm):
    date = DateField('Fecha')
    time = TimeField('Hora')
    moneda_from = SelectField('Moneda origen', choices=MONEDAS, validators=[DataRequired(message='Seleccione moneda de origen')])
    moneda_to = SelectField('Moneda deseada', choices=MONEDAS, validators=[DataRequired(message='Seleccione moneda deseada')])
    
    cantidad_to = FloatField('Cantidad')
    cantidad_from = FloatField('Cantidad', validators=[DataRequired(message='Ingrese cantidad deseada')])
    calculate = SubmitField('Calcular')
    precio_unitario = FloatField('Precio Unitario')
    submit = SubmitField('Ejecutar transacción')