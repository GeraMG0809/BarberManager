
class Cita:

    def __init__(self,datos:tuple)->None:
        self.id_cita = datos[1]
        self.id_barb = datos[2]
        self.id_usuario = datos[3]
        self.hora = datos[4]
        self.fecha = datos[5]

    def to_dict(self):
        return{'id_cita':self.id_cita,
               'id_barb':self.id_barb,
               'id_usuario':self.id_usuario,
               'hora':self.hora,
               'fecha':self.fecha}
    
    def from_dict(cls,data):
        return cls(data['id_cita'],
                   data['id_barb'],
                   data['id_usuario'],
                   data['hora'],
                   data['fecha'])