from datetime import date, datetime
from flask import render_template, request, redirect, flash
from registros_crip import app
from registros_crip.models import *
from registros_crip.forms import MovementsForm
from registros_crip.models_class import *


@app.route('/')
def index():
    dic = select_all()

    return render_template('index.html', datos=dic)

@app.route('/purchase', methods=['GET','POST'])
def purchase():
    if request.method == 'GET':
        form = MovementsForm()
        form.moneda_to.default = 'BTC'
        form.process()
        movimientos = select_all

        return render_template('purchase.html', dataForm=form, data=movimientos)
    else:
        form = MovementsForm(data=request.form)
        moneda_from = form.moneda_from.data
        moneda_to = form.moneda_to.data
        cantidad = form.cantidad_from.data
        
        exchange = CryptoExchange(moneda_from, moneda_to)
        rate = exchange.getRate()
        cantidad_to = cantidad*rate
        precio_unitario = cantidad/cantidad_to
        monedas_disponibles = cripto_individual_ganada(cripto=moneda_from) - cripto_from(cripto=moneda_from)
        
        def validateForm(form):
            errores = []
            if moneda_from == moneda_to:
                errores.append('Seleccione monedas distintas')
            elif cantidad > monedas_disponibles and moneda_from != 'EUR':
                errores.append(f'La cantidad a comprar de {moneda_from} debe ser igual o menor a los fondos de los que dispone')
                errores.append(f'Actualmente dispone de {formato_cantidad(monedas_disponibles)} {moneda_from} en myCrynversiones')
            return errores
        
        error = validateForm(request.form)
        if error:
            return render_template('purchase.html', dataForm=form, errors=error)

        if form.calculate.data:
            return render_template('purchase.html', dataForm=form, rate=formato_cantidad(rate), cantidad_to=formato_cantidad(cantidad_to),precio_unitario=formato_cantidad(precio_unitario),
                                   moneta_to=moneda_to, moneda_from=moneda_from, cantidad=formato_cantidad(cantidad), monedas_disponibles=monedas_disponibles)
        
        if form.validate_on_submit():
            fecha = date.today()
            now = datetime.now()
            hora = now.strftime('%H:%M:%S')
            save([fecha,hora,moneda_from,cantidad,moneda_to,cantidad_to,precio_unitario])
            flash('Transacción registrada')
            return redirect('/')
        else:

            return render_template('purchase.html', errors={}, dataForm=form)

@app.route('/status')
def status():
    return render_template('status.html', invertido = euros_gastados(), recuperado = euros_ganados(), valorCompraBruto= euros_gastados_bruto() - euros_ganados_bruto(),
                            valorCompra = formato_cantidad(euros_gastados_bruto() - euros_ganados_bruto()), valorActual = formato_cantidad(CryptoSuma().rateMyCripto()),
                            valorActualBruto = CryptoSuma().rateMyCripto())