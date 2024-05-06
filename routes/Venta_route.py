from flask import Blueprint, jsonify, request, session,redirect, render_template, url_for
from utils.mensaje_error import formato_error
# Entidades
from models.entidades.Venta_ent import Venta,Credito
#from models.entidades.Contrato_ent import Contrato,PagoContrato
# Modelos
from models.Venta_model import Venta_modelo

venta = Blueprint('venta_bp', __name__)

@venta.route('/')
def venta_principal():
    return render_template('venta/venta.html')

@venta.route('/registro_venta', methods=['GET', 'POST'])
def registro_venta():
    if request.method == 'POST':
        #data es el tipo de datos que traera el post
        data = request.json
        precio_venta = data.get('precio_venta')
        id_cliente = data.get('id_cliente')
        id_tipo_venta = data.get('id_tipo_venta') # 1 es al contado y 2 es al credito
        id_encargado_ventas = session['id_personal']
        id_sector = data.get('id_sector')
        id_pasillo = data.get('id_pasillo')
        
        ent_venta = Venta(precio_venta=precio_venta,estado='P',id_cliente=id_cliente,id_tipo_venta=id_tipo_venta,
                          id_encargado_ventas=id_encargado_ventas,id_sector=id_sector,id_pasillo=id_pasillo)
        
        resultado = Venta_modelo.registrar_venta(ent_venta)
        if resultado[0]:
            respuesta = {'exito':True ,'titulo':'Exito', 'mensaje':'Registro exitoso!',
                         'redireccion': '/venta/registro_venta'}
            return jsonify(respuesta)
        else:
            error= formato_error(resultado[1])
            respuesta = {'exito':False ,'titulo':'Error', 'mensaje':error}
            return jsonify(respuesta)        
    else:
        return render_template('venta/reg_venta.html')

@venta.route('/registro_credito', methods=['POST'])
def registro_credito():
    if request.method == 'POST':
        #data es el tipo de datos que traera el post
        data = request.json
        precio_venta = data.get('precio_venta')
        id_cliente = data.get('id_cliente')
        id_tipo_venta = data.get('id_tipo_venta') # 1 es al contado y 2 es al credito
        id_encargado_ventas = session['id_personal']
        id_sector = data.get('id_sector')
        id_pasillo = data.get('id_pasillo')
        ent_venta = Venta(precio_venta=precio_venta,estado='P',id_cliente=id_cliente,id_tipo_venta=id_tipo_venta,
                          id_encargado_ventas=id_encargado_ventas,id_sector=id_sector,id_pasillo=id_pasillo)
        
        cantidad_cuotas = data.get('cantidad_cuotas')
        monto = data.get('monto')
        fecha_inicio = data.get('fecha_inicio')
        tasa_interes_anual = data.get('tasa_interes_anual')
        ent_credito = Credito(cantidad_cuotas=cantidad_cuotas,monto=monto,fecha_inicio=fecha_inicio,
                              tasa_interes_anual=tasa_interes_anual)
        
        resultado = Venta_modelo.registrar_venta_credito(ent_venta,ent_credito)
        if resultado[0]:
            respuesta = {'exito':True ,'titulo':'Exito', 'mensaje': resultado[1],
                         'redireccion': '/venta/registro_venta'}
            return jsonify(respuesta)
        else:
            error= formato_error(resultado[1])
            respuesta = {'exito':False ,'titulo':'Error', 'mensaje':error}
            return jsonify(respuesta)        
    
@venta.route('/traer_locales_comercial', methods=['GET'])
def traer_locales_comercial():
    respuesta = Venta_modelo.traer_locales_comercial()
    return jsonify(respuesta)

@venta.route('/traer_tipo_venta', methods=['GET'])
def traer_tipo_venta():
    respuesta = Venta_modelo.traer_tipo_venta()
    return jsonify(respuesta)

@venta.route('/buscar_cliente_venta/<nro_ci>', methods=['GET'])
def buscar_cliente_venta(nro_ci):
    resultado = Venta_modelo.buscar_cliente_venta(nro_ci)
    if resultado[0]:
        respuesta = {'exito':True ,'contenido': resultado[1]}
        return jsonify(respuesta)
    else:
        respuesta = {'exito':False ,'contenido': resultado[1]}
        return jsonify(respuesta)
