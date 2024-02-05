from registros_crip import app
from flask import render_template, request, redirect, flash
from registros_crip.models import *
from datetime import date, time
from config import APIKEY
from registros_crip.forms import MovementsForm
from registros_crip.models_class import *


def validarFormulario(datosFormularios):
    errores = []#Crear lista para guardar errores
    
    if datosFormularios['moneda_from'] == 0:
        errores.append('Seleccione una moneda')
    if datosFormularios['cantidad_from'] == 0:
        errores.append('La cantidad no puede ir vacío')
    if datosFormularios['moneda_to'] == '':
        errores.append('Seleccione una moneda')
    if datosFormularios['cantidad_to'] == '':
        errores.append('La cantidad no puede de vacío')

    return errores

@app.route('/')#mostrará una tabla con los movimientos (compras y conversiones de criptomonedas) realizados por el usuario
def index():
    dic = select_all()

    return render_template('index.html', datos=dic)

@app.route('/purchase', methods=['GET','POST'])
def purchase():
    
    if request.method == 'GET':
        form = MovementsForm()
        return render_template('purchase.html', dataForm=form)
        #return render_template('purchase.html', dataForm=form, EUR=getEUR(), BTC=getBTC(), ETH=getETH(), USDT=getUSDT(), 
                               #BNB=getBNB(), XRP=getXRP(), ADA=getADA(), SOL=getSOL(), DOT=getDOT(), MATIC=getMATIC())
    else:#post
        form = MovementsForm(data=request.data)
        moneda_from = form.moneda_from.data
        moneta_to = form.moneda_to.data
        cantidad = form.cantidad_from.data
        exchange = CryptoExchange(moneda_from, moneta_to)

        rate = exchange.getRate()
        cantidad_to = cantidad*rate
        precio_unitario = cantidad/cantidad_to

        cantidad_to_formateada = f'{cantidad_to:.6f}'
        rate_formateado = f'{rate:.6f}'
        pu_formateado = f'{precio_unitario:.6f}'

        if form.calculate.data:

            return render_template('purchase.html', dataForm=form, rate=rate_formateado, cantidad_to=cantidad_to_formateada,precio_unitario=pu_formateado,
                                   moneta_to=moneta_to, moneda_from=moneda_from, cantidad=cantidad)
        
        if form.submit.data:
            pass

            #return render_template('purchase.html', errors=errores, dataForm=form, rate = getRate(), EUR=getEUR(), BTC=getBTC(),
                                    #ETH=getETH(), USDT=getUSDT(), BNB=getBNB(), XRP=getXRP(),ADA=getADA(), SOL=getSOL(), DOT=getDOT(), MATIC=getMATIC())
            
        
    return redirect('/')

@app.route('/status')
def status():
    return render_template('status.html')
