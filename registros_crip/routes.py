from registros_crip import app
from flask import render_template
from registros_crip.models import *

@app.route('/')#mostrará una tabla con los movimientos (compras y conversiones de criptomonedas) realizados por el usuario
def index():
    dic = select_all()
    
    return render_template('index.html', datos=dic)


@app.route('/purchase', methods=['GET','POST'])
def purchase():
    return 'Aquí se hacen las transacciones'

@app.route('/status')
def status():
    return 'Aquí se mira el estado de mis inversiones'