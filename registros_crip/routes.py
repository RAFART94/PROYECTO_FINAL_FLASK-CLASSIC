from registros_crip import app
from flask import render_template, request, redirect, flash
from registros_crip.models import *
from datetime import date, time
from config import APIKEY
from registros_crip.forms import MovementsForm


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
    form = MovementsForm()
    if request.method == 'GET':
        return render_template('purchase.html', dataForm=form, EUR=getEUR(), BTC=getBTC(), ETH=getETH(), USDT=getUSDT(), 
                               BNB=getBNB(), XRP=getXRP(), ADA=getADA(), SOL=getSOL(), DOT=getDOT(), MATIC=getMATIC())
    else:#post
        errores = validarFormulario(request.form)
        if errores:
            return render_template('purchase.html', errors=errores, dataForm=form, rate = getRate(), EUR=getEUR(), BTC=getBTC(),
                                    ETH=getETH(), USDT=getUSDT(), BNB=getBNB(), XRP=getXRP(),ADA=getADA(), SOL=getSOL(), DOT=getDOT(), MATIC=getMATIC())
            
        
    return redirect('/')

@app.route('/status')
def status():
    return render_template('status.html')
