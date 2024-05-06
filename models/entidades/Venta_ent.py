class Venta:
    def __init__(self, id=None, fecha_registro=None, precio_venta=None, estado=None, id_cliente=None, id_tipo_venta=None, id_encargado_ventas=None, id_sector=None, id_pasillo=None):
        self.id = id
        self.fecha_registro = fecha_registro
        self.precio_venta = precio_venta
        self.estado = estado
        self.id_cliente = id_cliente
        self.id_tipo_venta = id_tipo_venta
        self.id_encargado_ventas = id_encargado_ventas
        self.id_sector = id_sector
        self.id_pasillo = id_pasillo
    
    def convertir_JSON(self):
        return {
            'id': self.id,
            'fecha_registro': self.fecha_registro,
            'precio_venta': self.precio_venta,
            'estado': self.estado,
            'id_cliente': self.id_cliente,
            'id_tipo_venta': self.id_tipo_venta,
            'id_encargado_ventas': self.id_encargado_ventas,
            'id_sector': self.id_sector,
            'id_pasillo': self.id_pasillo
        }

class Credito:
    def __init__(self, id=None, cantidad_cuotas=None, monto=None, fecha_registro=None, fecha_inicio=None, fecha_fin=None, estado=None, tasa_interes_anual=None, id_venta=None):
        self.id = id
        self.cantidad_cuotas = cantidad_cuotas
        self.monto = monto
        self.fecha_registro = fecha_registro
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.tasa_interes_anual = tasa_interes_anual
        self.id_venta = id_venta
    
    def convertir_JSON(self):
        return {
            'id': self.id,
            'cantidad_cuotas': self.cantidad_cuotas,
            'monto': self.monto,
            'fecha_registro': self.fecha_registro,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin,
            'estado': self.estado,
            'tasa_interes_anual': self.tasa_interes_anual,
            'id_venta': self.id_venta
        }
