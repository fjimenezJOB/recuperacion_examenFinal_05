from wtforms import Form
from wtforms import TextField
from wtforms import PasswordField
from wtforms import validators
from wtforms import StringField
from wtforms import HiddenField
from wtforms.fields.html5 import EmailField


def honeypot_len(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('ATAQUE DE BOT CACA')


class formulario(Form):
    nombre = StringField('Nombre: ', [
        validators.required('Es obligatorio'),
        validators.length(min=5, max=30, message='Nombre no valido!!')
    ])
    apellido = StringField('Apellidos: ', [
        validators.required('Es obligatorio'),
        validators.length(min=5, max=30, message='Nombre demasiado largo!!')
    ])
    direccion = TextField('Dirección: ', [
        validators.required('Dirección requerida!!'),
        validators.length(min=10, max=100, message='Dirección muy larga!!')
    ])
    localidad = TextField('Localidad: ', [
        validators.required('Localidad Requerida!!'),
        validators.length(min=10, max=100, message='Localidad muy larga!!')
    ])
    nacionalidad = TextField('Nacionalidad: ', [
        validators.required('Nacionalidad Requerida!!'),
        validators.length(min=10, max=100, message='Nacionalidad muy larga!!')

    ])
    email = EmailField('Email: ', [
        validators.required('Es Obligatorio'),
        validators.email('Ingrese su Email valido!')
    ])
    dni = TextField('DNI (00000000T): ', [
        validators.length(
            min=0, max=9, message='Se excede del limite permitido.')
    ])
    password = PasswordField('Contraseña: ', [
        validators.required('Campo requerido')
    ])
    # trampa honeypot
    honeypot = HiddenField('', [honeypot_len])
