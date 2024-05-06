from database.db import conectar_bd
from utils.formato_time import fecha_hora, fecha

class Pago_modelo():
    
    @classmethod
    def registrar_pago_contado(cls, pago):
        try:
            conn = conectar_bd()
            with conn.cursor() as cursor:
                cursor.execute("""INSERT INTO pago_contado (fecha_registro, monto, observacion, id_venta) 
                VALUES (NOW(), %s, %s, %s);""", 
                (pago.monto,pago.observacion,pago.id_venta))
                conn.commit()
            conn.close()
            return [True, 'Registro exitoso!']
        except Exception as ex:
            print(ex)
            return [False,ex]
        
    @classmethod
    def registrar_pago_credito(cls, pago):
        try:
            conn = conectar_bd()
            with conn.cursor() as cursor:
                cursor.execute("""INSERT INTO pago_cuota (fecha_registro, monto, observacion, id_cuota) 
                VALUES (NOW(), %s, %s, %s);""", 
                (pago.monto,pago.observacion,pago.id_cuota))
                conn.commit()
            conn.close()
            return [True, 'Registro exitoso!']
        except Exception as ex:
            print(ex)
            return [False,ex]
    
    @classmethod    
    def traer_venta_contado_nro_ci(cls,id_tipo_venta,nro_ci):    
        try:
            conn = conectar_bd()
            datos_consulta = [False, 'No existen Pagos pendientes del cliente!']
            with conn.cursor() as cursor:
                cursor.execute("""SELECT v.id, v.fecha_registro, v.precio_venta, lc.nro_local, CONCAT(p.nombres,' ',p.p_apellido) as nombre_cliente
                FROM venta v
                JOIN cliente cl ON v.id_cliente = cl.id
                JOIN persona p ON p.id = cl.id
                JOIN local_comercial lc ON lc.id_sector = v.id_sector AND lc.id_pasillo = v.id_pasillo
                WHERE v.estado='P' AND v.id_tipo_venta = %s AND p.nro_ci = %s;""",(id_tipo_venta,nro_ci,))
                resultado = cursor.fetchall()
                if resultado:
                    resultado_consulta=[]
                    for fila in resultado:
                        dato = {
                            'id_venta': fila[0],
                            'fecha_registro': fecha_hora(fila[1]),
                            'precio_venta': fila[2],
                            'nro_local': fila[3],
                            'nombre_cliente': fila[4]
                        }
                        resultado_consulta.append(dato)
                    datos_consulta=[True,resultado_consulta]
            conn.close()
            return datos_consulta
        except Exception as ex:
            print(ex)
    
    @classmethod    
    def traer_cuotas_credito(cls,id_venta):    
        try:
            conn = conectar_bd()
            datos_consulta = [False, 'No existen Pagos pendientes del cliente!']
            with conn.cursor() as cursor:
                cursor.execute("""SELECT cu.id, cu.nro_cuota, cu.fecha_pago, cu.estado , cu.monto_capital, cu.monto_interes,cu.monto_mora,
                    CASE
                        WHEN cu.estado = 'P' AND ant.estado = 'P' THEN 'S'
                        ELSE 'N'
                    END AS pagar_cuota_anterior
                FROM credito cr 
                JOIN venta v ON v.id = cr.id_venta
                JOIN cuota cu ON cu.id_credito = cr.id
                LEFT JOIN cuota ant ON cu.id_credito = ant.id_credito AND cu.nro_cuota = ant.nro_cuota + 1
                WHERE v.id = %s AND cu.estado= 'P'
                ORDER BY cu.nro_cuota;""",(id_venta,))
                resultado = cursor.fetchall()
                if resultado:
                    resultado_consulta=[]
                    for fila in resultado:
                        dato = {
                            'id_cuota': fila[0],
                            'nro_cuota': fila[1],
                            'fecha_pago': fecha(fila[2]),
                            'estado': fila[3],
                            'monto_capital': fila[4],
                            'monto_interes': fila[5],
                            'monto_mora': fila[6],
                            'pagar_cuota_anterior': fila[7]
                        }
                        resultado_consulta.append(dato)
                    datos_consulta=[True,resultado_consulta]
            conn.close()
            return datos_consulta
        except Exception as ex:
            print(ex)       
    