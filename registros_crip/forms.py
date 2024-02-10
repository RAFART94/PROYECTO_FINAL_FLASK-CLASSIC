from flask import Flask
from flask_wtf import FlaskForm
from wtforms import DateField,FloatField,SubmitField,TimeField,SelectField
from wtforms.validators import DataRequired,ValidationError
from config import *
from registros_crip.models import *
from registros_crip.models_class import *
from registros_crip.conexion import Conexion


MONEDAS = [('EUR', 'Euro (EUR)'), ('DOT','Polkadot (DOT)'), ("XRP", "Ripple (XRP)"),
            ('BTC', 'Bitcoin (BTC)'), ('ETH', 'Ethereum (ETH)'), ('SOL','Solana (SOL)'),
            ('MATIC', 'Polygon (MATIC)'),  ('USDT', 'Tether (USDT)'), ('BNB', 'Binance Coin (BNB)'),
            ('ADA', 'Cardano (ADA)')]

def MonedasDisponibles():
    conexion = Conexion('select moneda_to from Criptomovimientos where moneda_to != "EUR" group by moneda_to')
    lista_monedas = conexion.res.fetchall()
    monedas_from = [('EUR', 'Euro (EUR)')]
    for moneda in lista_monedas:
        if moneda[0] == 'BTC':
            monedas_from.append(("BTC", "Bitcoin (BTC)"))
        if moneda[0] == 'DOT':
            monedas_from.append(("DOT", "Polkadot (DOT)"))
        if moneda[0] == 'XRP':
            monedas_from.append(("XRP", "Ripple (XRP)"))
        if moneda[0] == 'ETH':
            monedas_from.append(("ETH", "Ethereum (ETH)"))
        if moneda[0] == 'SOL':
            monedas_from.append(("SOL", "Solana (SOL)"))
        if moneda[0] == 'MATIC':
            monedas_from.append(("MATIC", "Polygon (MATIC)"))
        if moneda[0] == 'USDT':
            monedas_from.append(("USDT", "Tether (USDT)"))
        if moneda[0] == 'BNB':
            monedas_from.append(("BNB", "Binance Coin (BNB)"))
        if moneda[0] == 'ADA':
            monedas_from.append(("ADA", "Cardano (ADA)"))
    
    conexion.con.commit()
    conexion.con.close()
        
    return monedas_from

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