from flask import Blueprint, jsonify, request, session,redirect, render_template, url_for
from utils.mensaje_error import formato_error
# Entidades
from models.entidades.Pago_ent import PagoContado,PagoCuota
# Modelos
from models.Pago_model import Pago_modelo

pago = Blueprint('pago_bp', __name__)

@pago.route('/')
def pago_principal():
    return render_template('pago/pago.html')

@pago.route('/registro_pago_contado', methods=['GET', 'POST'])
def registro_pago_contado():
    if request.method == 'POST':
        #data es el tipo de datos que traera el post
        data = request.json
        id_venta = data.get('id_venta')
        precio_venta = data.get('precio_venta')
        observacion = data.get('observacion')
        if  id_venta == '' or precio_venta == '':
            respuesta = {'exito':False ,'titulo':'Error', 'mensaje':'Complete todos los campos!'}
            return jsonify(respuesta)   
        ent_pago_contado = PagoContado(id_venta=id_venta,monto=precio_venta,observacion=observacion)
        
        resultado = Pago_modelo.registrar_pago_contado(ent_pago_contado)
        if resultado[0]:
            respuesta = {'exito':True ,'titulo':'Exito', 'mensaje':resultado[1],
                         'redireccion': '/pago/registro_pago_contado'}
            return jsonify(respuesta)
        else:
            error= formato_error(resultado[1])
            respuesta = {'exito':False ,'titulo':'Error', 'mensaje':error}
            return jsonify(respuesta)      
    else:
        return render_template('pago/reg_pago_contado.html')
    
@pago.route('/traer_venta_contado_nro_ci/<nro_ci>', methods=['GET'])
def traer_venta_contado_nro_ci(nro_ci):
    resultado = Pago_modelo.traer_venta_contado_nro_ci(1,nro_ci)
    if resultado[0]:
        respuesta = {'exito':True ,'contenido': resultado[1]}
        return jsonify(respuesta)
    else:
        respuesta = {'exito':False ,'contenido': resultado[1]}
        return jsonify(respuesta)
    
@pago.route('/traer_venta_credito_nro_ci/<nro_ci>', methods=['GET'])
def traer_venta_credito_nro_ci(nro_ci):
    resultado = Pago_modelo.traer_venta_contado_nro_ci(2,nro_ci)
    if resultado[0]:
        respuesta = {'exito':True ,'contenido': resultado[1]}
        return jsonify(respuesta)
    else:
        respuesta = {'exito':False ,'contenido': resultado[1]}
        return jsonify(respuesta)
    
@pago.route('/registro_pago_credito', methods=['GET', 'POST'])
def registro_pago_credito():
    if request.method == 'POST':
        #data es el tipo de datos que traera el post
        data = request.json
        id_cuota = data.get('id_cuota')
        monto = data.get('monto')
        observacion = data.get('observacion')
        if  id_cuota == '' or monto == '':
            respuesta = {'exito':False ,'titulo':'Error', 'mensaje':'Complete todos los campos!'}
            return jsonify(respuesta)   
        
        ent_pago_credito = PagoCuota(id_cuota=id_cuota,monto=monto,observacion=observacion)
        
        resultado = Pago_modelo.registrar_pago_credito(ent_pago_credito)
        if resultado[0]:
            respuesta = {'exito':True ,'titulo':'Exito', 'mensaje':resultado[1],
                         'redireccion': '/pago/registro_pago_credito'}
            return jsonify(respuesta)
        else:
            error= formato_error(resultado[1])
            respuesta = {'exito':False ,'titulo':'Error', 'mensaje':error}
            return jsonify(respuesta)      
    else:
        return render_template('pago/reg_pago_credito.html')
    
@pago.route('/traer_cuotas_credito/<id_venta>', methods=['GET'])
def traer_cuotas_credito(id_venta):
    resultado = Pago_modelo.traer_cuotas_credito(id_venta)
    if resultado[0]:
        respuesta = {'exito':True ,'contenido': resultado[1]}
        return jsonify(respuesta)
    else:
        respuesta = {'exito':False ,'contenido': resultado[1]}
        return jsonify(respuesta)
