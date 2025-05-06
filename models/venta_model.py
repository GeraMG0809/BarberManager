class Venta:
    def __init__(self,datos:tuple) -> None:
        self.id_venta = datos[0]
        self.id_cita = datos[1]
        self.fecha = datos[2]
        self.tipo_pago = datos[3]
        self.monto_final = datos[4]
        self.estado = datos[5]

    def to_dict(self):
        return{'id_venta': self.id_venta,
               'id_cita': self.id_cita,
               'fecha': self.fecha,
               'tipo_pago': self.tipo_pago,
               'monto_final': self.monto_final,
               'estado': self.estado}
    

    @classmethod
    def from_dict(cls,data):
        return cls(data['id_venta'],
                   data['id_cita'],
                   data['fecha'],
                   data['tipo_pago'],
                   data['monto_final'],
                   data['estado'])