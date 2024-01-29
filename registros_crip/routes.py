from registros_crip import app
from flask import render_template

@app.route('/')#mostrará una tabla con los movimientos (compras y conversiones de criptomonedas) realizados por el usuario
def index():
    diccionario = [{'Fecha':'01-01-2024', 'Hora':'14:50:37', 'From':'EUR', 'Q':7625.15, 'To':'BTC', 'Q':1.00, 'P.U':7625.15},
                   {'Fecha':'04-01-2024', 'Hora':'11:20:22', 'From':'BTC', 'Q':0.13, 'To':'LTC', 'Q':20.00, 'P.U':0.0067},
                   {'Fecha':'09-01-2024', 'Hora':'19:31:58', 'From':'BTC', 'Q':0.87, 'To':'ETH', 'Q':45.00, 'P.U':0.019}]
    return render_template('index.html', variable=diccionario)

@app.route('/purcharse', methods=['GET','POST'])
def purcharse():
    pass

@app.route('/status')
def status():
    pass