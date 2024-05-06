from database.db import conectar_bd

class Venta_modelo():

    @classmethod
    def registrar_venta(cls, venta):
        try:
            conn = conectar_bd()
            with conn.cursor() as cursor:
                cursor.execute("""INSERT INTO venta (fecha_registro, precio_venta, estado, id_cliente, 
                id_tipo_venta, id_encargado_ventas, id_sector, id_pasillo)
                VALUES (NOW(), %s, %s, %s, %s, %s, %s, %s);""", 
                (venta.precio_venta,venta.estado,venta.id_cliente,venta.id_tipo_venta,
                 venta.id_encargado_ventas,venta.id_sector,venta.id_pasillo))
                id_venta = cursor.lastrowid
                conn.commit()
            conn.close()
            return [True, id_venta]
        except Exception as ex:
            print(ex)
            return [False,ex]
        
    @classmethod
    def registrar_venta_credito(cls, venta,credito):
        try:
            id_venta = Venta_modelo.registrar_venta(venta)
            if id_venta[0] == True:
                conn = conectar_bd()
                with conn.cursor() as cursor:
                    cursor.execute('call registro_credito_generar_cuota(%s, %s, %s, %s, %s)',
                                (credito.cantidad_cuotas,credito.monto,credito.fecha_inicio,
                                    credito.tasa_interes_anual,id_venta[1]))
                    conn.commit()
                conn.close()
                return [True,'Registro Exitoso!']
            else:
                return [False, id_venta[1]]
        except Exception as ex:
            print(ex)
            return [False, ex]
        
    @classmethod
    def registrar_venta_segun_tipo(cls, venta):
        try:
            conn = conectar_bd()
            with conn.cursor() as cursor:
                cursor.execute("""INSERT INTO venta (fecha_registro, precio_venta, estado, id_cliente, 
                id_tipo_venta, id_encargado_ventas, id_sector, id_pasillo)
                VALUES (NOW(), %s, %s, %s, %s, %s, %s, %s);""", 
                (venta.precio_venta,venta.estado,venta.id_cliente,venta.id_tipo_venta,
                 venta.id_encargado_ventas,venta.id_sector,venta.id_pasillo))
                id_venta = cursor.lastrowid
                conn.commit()
            conn.close()
            return [True, id_venta]
        except Exception as ex:
            print(ex)
            return [False,ex]
    
    @classmethod    
    def buscar_cliente_venta(cls,nro_ci):    
        try:
            conn = conectar_bd()
            datos_consulta = [False, 'No existe el nro_ci!']
            with conn.cursor() as cursor:
                cursor.execute("""SELECT cl.id as id_cliente, CONCAT(p.nombres,' ',p.p_apellido) as nombre,
                    CASE
                        WHEN v.estado = 'P' THEN 'S'
                        ELSE 'N'
                    END AS pago_pendiente
                FROM cliente cl JOIN persona p ON p.id = cl.id
                LEFT JOIN venta v ON v.id_cliente = cl.id
                WHERE p.nro_ci = %s;""",(nro_ci,))
                resultado = cursor.fetchall()
                if resultado:
                    for fila in resultado:
                        dato = {
                            'id_cliente': fila[0],
                            'nombre': fila[1],
                            'pago_pendiente': fila[2]
                        }
                        datos_consulta.append(dato)
                    datos_consulta=[True,dato]
            conn.close()
            return datos_consulta
        except Exception as ex:
            print(ex)
            
    @classmethod    
    def traer_locales_comercial(cls):    
        try:
            conn = conectar_bd()
            datos_consulta = []
            with conn.cursor() as cursor:
                cursor.execute("""SELECT lc.id_sector, lc.id_pasillo , lc.nro_local , lc.precio, lc.metros_cuadrados, 
                               lc.descripcion, lc.estado,s.nombre as sector, p.nombre as pasillo, pi.nombre as piso
                FROM local_comercial lc 
                JOIN sector s ON lc.id_sector = s.id
                JOIN pasillo p ON lc.id_pasillo = p.id
                JOIN piso pi ON p.id_piso = pi.id;""")
                resultado = cursor.fetchall()
                for fila in resultado:
                    dato = {
                        'id_sector': fila[0],
                        'id_pasillo': fila[1],
                        'nro_local': fila[2],
                        'precio': fila[3],
                        'metros_cuadrados': fila[4],
                        'descripcion': fila[5],
                        'estado': fila[6],
                        'sector': fila[7],
                        'pasillo': fila[8],
                        'piso': fila[9]
                    }
                    datos_consulta.append(dato)
            conn.close()
            return datos_consulta
        except Exception as ex:
            print(ex)
            
    @classmethod    
    def traer_tipo_venta(cls):    
        try:
            conn = conectar_bd()
            datos_consulta = []
            with conn.cursor() as cursor:
                cursor.execute("""SELECT tv.id, tv.nombre FROM tipo_venta tv;""")
                resultado = cursor.fetchall()
                for fila in resultado:
                    dato = {
                        'id': fila[0],
                        'nombre': fila[1]
                    }
                    datos_consulta.append(dato)
            conn.close()
            return datos_consulta
        except Exception as ex:
            print(ex)