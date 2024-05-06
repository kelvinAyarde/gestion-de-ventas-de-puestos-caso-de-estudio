class PagoContado:
    def __init__(self, id=None, fecha_registro=None, monto=None, observacion=None, id_venta=None):
        self.id = id
        self.fecha_registro = fecha_registro
        self.monto = monto
        self.observacion = observacion
        self.id_venta = id_venta
    
    def convertir_JSON(self):
        return {
            'id': self.id,
            'fecha_registro': self.fecha_registro,
            'monto': self.monto,
            'observacion': self.observacion,
            'id_venta': self.id_venta
        }

class PagoCuota:
    def __init__(self, id=None, fecha_registro=None, monto=None, observacion=None, id_cuota=None):
        self.id = id
        self.fecha_registro = fecha_registro
        self.monto = monto
        self.observacion = observacion
        self.id_cuota = id_cuota
    
    def convertir_JSON(self):
        return {
            'id': self.id,
            'fecha_registro': self.fecha_registro,
            'monto': self.monto,
            'observacion': self.observacion,
            'id_cuota': self.id_cuota
        }

