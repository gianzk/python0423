import models.modelsCase as md
import bcrypt

class UserController:

    def __init__(self):
        self.model=md.User()

    def getUsers(self):
        data=self.model.getUserAll()
        return data
    def getUser(self,id):
        data=self.model.getUser(id)
        return data
    def insertUser(self,data):
        print(data)
        data['password']=bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt(6))
        dataTuple=(data['usuario'],data['password'],data['email'],data['fullname'],data['tipousuario'])
        ### mucha logica
        self.model.insertUser(dataTuple)