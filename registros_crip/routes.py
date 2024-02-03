from registros_crip import app
from flask import render_template, request, redirect
from registros_crip.models import *
from registros_crip.models_class import *
from datetime import date, time
from config import APIKEY




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
    if dic:
        return render_template('index.html', datos=dic)
    else:
        return render_template('index.html', sindatos=dic)


@app.route('/purchase', methods=['GET','POST'])
def purchase():
    if request.method == 'GET':
        return render_template('purchase.html', dataForm={})
    else:
        errores = validarFormulario(request.form)
        if errores:
            return render_template('purchase.html', errors=errores, dataForm=request.form)
        
        insert([request.form['moneda_from'],
                request.form['cantidad_to'],
                request.form['moneda_to'],
                request.form['cantidad_to']])
        
        return redirect('/')

@app.route('/status')
def status():
    return render_template('status.html')
