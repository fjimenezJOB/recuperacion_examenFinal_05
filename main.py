from flask import Flask, render_template, request
from flask_wtf import CsrfProtect
import lib.form
from lib.conexion_bd import *


app = Flask(__name__)
app.secret_key = 'recuperacion'
csrf = CsrfProtect(app)

dni = ''

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global dni
        dni = request.form.get('dni')
        # dni_bd = leer_usuario(dni)
        password = request.form.get('password')
        pass_bd = leer_password(dni)

        if pass_bd == password:
            usuario = leer_usuario(dni)
            saldo = get_dinero(dni)
            context = {
                'nombre_completo': f'{usuario[0][1]} {usuario[0][2]} {usuario[0][3]}',
                'saldo': saldo
            }
            return render_template('cajero.html', **context)
        else:
            error = True
            return render_template('index.html', error=error)


@app.route('/retirar', methods=['GET','POST'])
def retirar():
    global dni
    dinero_acual = get_dinero(dni)
    context = {
        'saldo' : dinero_acual
    }
    if request.method == 'POST':
        dinero_ingresar = int(request.form.get('retiro'))
        saldo = dinero_acual - dinero_ingresar
        if saldo > 0:
            set_dinero(dni, saldo)
            return render_template('adios.html', saldo = saldo)

    return render_template('retirar.html', **context)


@app.route('/ingresar', methods=['POST','GET'])
def ingresar():
    global dni
    print(dni)
    dinero_acual = get_dinero(dni)
    if request.method == 'POST':
        dinero_ingresar = int(request.form.get('ingreso'))
        saldo = dinero_acual + dinero_ingresar
        if saldo > 0:
            set_dinero(dni, saldo)
            return render_template('adios.html', saldo = saldo)
    context = {
        'saldo' : dinero_acual
    }
    return render_template('ingresar.html', **context)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)