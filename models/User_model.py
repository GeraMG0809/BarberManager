
class User:
    def __init__(self, datos:tuple) ->None:
        self.id = datos[0]
        self.name = datos[1]
        self.email = datos[2]
        self.password = datos[3]
        self.status = datos[4]

    def to_dict(self):
        return {'id':self.id,
                'name':self.name,
                'email':self.email,
                'password':self.password,
                'status':self.status}
    

    def from_dict(cls,data):
        return cls(data['id'],
                   data['name'],
                   data['email'],
                   data['password'],
                   data['status'])