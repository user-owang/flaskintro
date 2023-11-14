# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

from operations import *

@app.route('/add')
def add_route():
  return str(add(int(request.args['a']), int(request.args['b'])))

@app.route('/sub')
def subtract_route():
  return str(sub(int(request.args['a']), int(request.args['b'])))

@app.route('/mult')
def mult_route():
  return str(mult(int(request.args['a']), int(request.args['b'])))

@app.route('/div')
def div_route():
  return str(div(int(request.args['a']), int(request.args['b'])))
