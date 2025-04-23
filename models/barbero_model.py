class Barbero:
    
    def __init__(self, datos: tuple) -> None:
        self.id_barbero = datos[0]
        self.nombre = datos[1]
        self.telefono = datos[2]
        self.imagenes = datos[3]
        self.estado = datos[4]
        # Valor temporal (puedes calcularlo luego con comentarios)
        self.calificacion = "4.5 ⭐"  

    def to_dict(self):
        return {
            'id_barbero': self.id_barbero,
            'nombre': self.nombre,
            'telefono': self.telefono,
            'imagenes': self.imagenes,
            'estado': self.estado,
            'calificacion': self.calificacion
        }

    @classmethod
    def from_dict(cls, data):
        return cls((
            data['id_barbero'],
            data['nombre'],
            data['telefono'],
            data['imagenes'],
            data['estado']
        ))
