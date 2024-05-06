from flask import Blueprint, jsonify, request, session,redirect, render_template, url_for
from utils.mensaje_error import formato_error
# Entidades
from models.entidades.Usuario_ent import Usuario
# Modelos
from models.Inicio_model import SesionUsuario

inicio = Blueprint('inicio_bp', __name__)

@inicio.route('/')
def home():
    if 'sesion_abierta' in session:
        return render_template('inicio/base.html')
    else:      
        return redirect(url_for('inicio_bp.login'))

@inicio.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json
        usuario = data.get('usuario')
        password = data.get('password')
        ent_usuario = Usuario(usuario=usuario,password=password)
        resultado = SesionUsuario.verificar_usuario(ent_usuario)
        if resultado[0]:
            respuesta = {'exito':True ,'titulo':'exito', 'mensaje':resultado[1],
                         'redireccion': '/'}
            return jsonify(respuesta)
        else:
            error= formato_error(resultado[1])
            respuesta= {'exito':False ,'titulo':'error', 'mensaje':error}
            return jsonify(respuesta)
    else:
        return render_template('inicio/login.html')

@inicio.route('/cerrar_sesion')
def cerrar_sesion():
    SesionUsuario.cerrar_sesion()
    return redirect(url_for('inicio_bp.home'))