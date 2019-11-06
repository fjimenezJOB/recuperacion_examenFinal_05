from flask import Flask, render_template, request
from flask_wtf import CsrfProtect
import lib.form
from lib.conexion_bd import *


app = Flask(__name__)
app.secret_key = 'recuperacion'
csrf = CsrfProtect(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        dni = request.form.get('dni')
        # dni_bd = leer_usuario(dni)
        password = request.form.get('password')
        pass_bd = leer_password(dni)
        print(pass_bd)

        if pass_bd == password:
            return render_template('cajero.html')
        else:
            error = True
            return render_template('index.html', error = error)

@app.route('/retirar')
def retirar():
    render_template('retirar.html')
if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)