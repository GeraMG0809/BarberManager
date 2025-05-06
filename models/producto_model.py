class Producto:
    def __init__(self, datos: tuple) -> None:
        self.id_producto = datos[0]
        self.categoria = datos[1]
        self.precio = datos[2]
        self.estado = datos[3]
        self.nombre_producto = datos[4]

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'categoria': self.categoria,
            'precio': self.precio,
            'estado': self.estado,
            'nombre_producto': self.nombre_producto
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls((
            data['id_producto'],
            data['categoria'],
            data['precio'],
            data['estado'],
            data['nombre_producto']
        ))
