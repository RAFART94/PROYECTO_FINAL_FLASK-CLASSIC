from flask import Flask

app = Flask(__name__)

from registros_crip.routes import *