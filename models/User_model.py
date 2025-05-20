class User:
    def __init__(self, datos:tuple) ->None:
        self.id = datos[0]
        self.name = datos[1]
        self.telefono = datos[2]
        self.email = datos[3]
        self.password = datos[4]
        self.status = datos[5]

    def to_dict(self):
        return {'id':self.id,
                'name':self.name,
                'telefono':self.telefono,
                'email':self.email,
                'password':self.password,
                'status':self.status}
    

    @classmethod
    def from_dict(cls,data):
        return cls((
            data['id'],
            data['name'],
            data['telefono'],
            data['email'],
            data['password'],
            data['status']
        ))