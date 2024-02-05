from registros_crip import app
from flask import Flask,render_template, request, redirect, flash
from registros_crip.models import *
from datetime import date, datetime, time
from config import APIKEY
from registros_crip.forms import MovementsForm, MONEDAS, ValidationError
from registros_crip.models_class import *


@app.route('/')#mostrará una tabla con los movimientos (compras y conversiones de criptomonedas) realizados por el usuario
def index():
    dic = select_all()

    return render_template('index.html', datos=dic)

@app.route('/purchase', methods=['GET','POST'])
def purchase():
    
    if request.method == 'GET':
        form = MovementsForm()
        form.moneda_from.default = 'EUR'
        form.moneda_to.default = 'BTC'
        form.process()

        return render_template('purchase.html', dataForm=form)
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

        def validateForm(form):
            errores = []
            if moneda_from == moneta_to:
                errores.append('Seleccione monedas distintas')

            return errores
        
        error = validateForm(request.form)
        if error:
            return render_template('purchase.html', dataForm=form, errors=error)

        if form.calculate.data:

            return render_template('purchase.html', dataForm=form, rate=rate_formateado, cantidad_to=cantidad_to_formateada,precio_unitario=pu_formateado,
                                   moneta_to=moneta_to, moneda_from=moneda_from, cantidad=cantidad)
        
        if form.validate_on_submit():
            fecha = date.today()
            now = datetime.now()
            hora = now.strftime('%H:%M:%S')
            save([fecha,hora,moneda_from,cantidad,moneta_to,cantidad_to_formateada,pu_formateado])

            flash('Movimiento registrado con éxito')

            return redirect('/')
        else:

            return render_template('purchase.html', errors={}, dataForm=form)


@app.route('/status')
def status():
    return render_template('status.html')
