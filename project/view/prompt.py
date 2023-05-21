from controller.UserController import * 
from controller.tipoCambio import *
def viewPrompt():
    data={
    'usuario':'',
    'password':'',
    'email':'',
    'fullname':''
    }

    data['usuario']=input('ingrese un usuario: ')
    data['password']=input('ingrese su password: ')
    data['email']=input('ingrese su email: ')
    data['fullname']=input('ingrese fullname: ')
    data['tipousuario']=input('ingrese el tipo de usuario: ')

    ctrl=UserController()
    ctrl.insertUser(data)

def TipodecambioView():
    ctrl=TipoCambio()
    ctrl.insertData()



