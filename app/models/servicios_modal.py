class Servicio:
    def __init__(self, datos: tuple) -> None:
        self.id_servicio = datos[0]
        self.servicios = datos[1]
        self.precio = datos[2]
        self.estado = datos[3]
        self.nombre_servicio = datos[4]


    def to_dict(self):
        return {
            'id_servicio': self.id_servicio,
            'nombre_servicio': self.nombre_servicio,
            'servicios': self.servicios,
            'precio': self.precio,
            'estado': self.estado
        }

    @classmethod
    def from_dict(cls, data):
        return cls((
            data['id_servicio'],
            data['nombre_servicio'],
            data['servicios'],
            data['precio'],
            data['estado']
        ))
