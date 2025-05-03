class Cita:

    def __init__(self, datos: tuple) -> None:
        self.id_cita = datos[0]
        self.cliente = datos[1]
        self.barbero = datos[2]
        self.servicio = datos[3]
        self.precio = datos[4]
        self.fecha = datos[5]
        self.hora = datos[6]
        self.estado = datos[7]

    def to_dict(self):
        return {
            'id_cita': self.id_cita,
            'cliente': self.cliente,
            'barbero': self.barbero,
            'servicio': self.servicio,
            'precio': self.precio,
            'fecha': self.fecha,
            'hora': self.hora,
            'estado': self.estado
        }

    @classmethod
    def from_dict(cls, data):
        return cls((
            data['id_cita'],
            data['cliente'],
            data['barbero'],
            data['servicio'],
            data['precio'],
            data['fecha'],
            data['hora'],
            data['estado']
        ))
