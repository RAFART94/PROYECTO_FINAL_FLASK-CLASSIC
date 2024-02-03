from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField,TimeField,SelectField
from wtforms.validators import DataRequired,Length,ValidationError
from datetime import date

MONEDAS = [('EUR', 'Euro (EUR)'), ('ADA', 'Cardano (ADA)'), ('BNB', 'Binance Coin (BNB)'),
         ('BTC', 'Bitcoin (BTC)'), ('DOT','Polkadot (DOT)'), ('ETH', 'Ethereum (ETH)'),
         ('MATIC', 'Polygon (MATIC)'), ('SOL','Solana (SOL)'), ('USDT', 'Tether (USDT)'),
         ("XRP", "XRP (XRP)")]

class MovementsForm(FlaskForm):
    date = DateField('Fecha')
    time = TimeField('Hora')
    moneda_from = SelectField('Moneda origen', seleccionar=MONEDAS, validators=[DataRequired(message='Seleccione moneda de origen')])
    moneda_to = SelectField('Moneda deseada', seleccionar=MONEDAS, validators=[DataRequired(message='Seleccione moneda deseada')])
    cantidad_from = FloatField('Cantidad', validators=[DataRequired(message='Ingrese cantidad deseada')])

    submit = SubmitField('Ejecutar transacción')