
class Cita:

    def __init__(self,datos:tuple)->None:
        self.id_cita = datos[0]
        self.id_barb = datos[1]
        self.id_usuario = datos[2]
        self.hora = datos[3]
        self.fecha = datos[4]

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