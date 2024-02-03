from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

ORIGIN_DATA='data/movements.sqlite'

from registros_crip.routes import *