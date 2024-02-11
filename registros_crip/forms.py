from flask_wtf import FlaskForm
from wtforms import DateField,FloatField,SubmitField,TimeField,SelectField
from wtforms.validators import DataRequired


MONEDAS = [('EUR', 'Euro (EUR)'), ('DOT','Polkadot (DOT)'), ("XRP", "Ripple (XRP)"),
            ('BTC', 'Bitcoin (BTC)'), ('ETH', 'Ethereum (ETH)'), ('SOL','Solana (SOL)'),
            ('MATIC', 'Polygon (MATIC)'),  ('USDT', 'Tether (USDT)'), ('BNB', 'Binance Coin (BNB)'),
            ('ADA', 'Cardano (ADA)')]

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