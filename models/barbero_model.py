

class Barbero:
    
    def __init__(self,datos:tuple)->None:
        self.id_barbero = datos[0]
        self.nombre_barbero = datos[1]
        self.telefono = datos[2]
        self.imagenes = datos[3]
    
    def to_dict(self):
        return{'id_barbero':self.id_barbero,
               'nombre_cliente':self.nombre_barbero,
               'telefono':self.telefono,
               'imagenes':self.imagenes}

    def from_dict(cls,data):
        return cls(data['id_barbero'],
                   data['nombre_barbero'],
                   data['telefono'],
                   data['imagenes'])
      