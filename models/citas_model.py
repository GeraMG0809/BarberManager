class Cita:

    def __init__(self, datos: tuple) -> None:
        self.id_cita = datos[0]
        self.cliente = datos[1]
        self.barbero = datos[2]
        self.servicio = datos[3]
        self.fecha = datos[4]
        self.hora = datos[5]
        self.estado = datos[6]

    def to_dict(self):
        return {
            'id_cita': self.id_cita,
            'cliente': self.cliente,
            'barbero': self.barbero,
            'servicio': self.servicio,
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
            data['fecha'],
            data['hora'],
            data['estado']
        ))
