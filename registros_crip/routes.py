from registros_crip import app
from flask import render_template, request, redirect
from registros_crip.models import *
from datetime import date, time



def validarFormulario(datosFormularios):
    errores = []#Crear lista para guardar errores
    hoy = str(date.today())#Esto quita la fecha de hoy
    
    if datosFormularios['date'] > hoy:
        errores.append('La fecha no puede ser mayor a la actual')
    if datosFormularios['time'] > hoy:
        errores.append('La hora no puede ser mayor a la actual')
    if datosFormularios['moneda_from'] == '':
        errores.append('El concepto no puede ir vacío')
    if datosFormularios['cantidad_from'] == '':
        errores.append('La cantidad no puede ir vacío')
    if datosFormularios['moneda_to'] == '':
        errores.append('El concepto no puede ir vacío')
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
        
        insert([request.form['date'],
                request.form['time'],
                request.form['moneda_from'],
                request.form['cantidad_to'],
                request.form['moneda_to'],
                request.form['cantidad_to']])
        
        return redirect('/')

@app.route('/status')
def status():
    return 'Aquí se mira el estado de mis inversiones'