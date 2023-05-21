

class Register:
    def __init__(self,name):
        self.nameFile=name
        
    def openFile(self):
        self.archivo=open(self.nameFile,"a")

    def guardarInfo(self,contenido:str):
        self.archivo.write(contenido)
        self.archivo.close()
    def mostrar(self):
        self.archivo=open(self.nameFile,"r")
        contenido=self.archivo.read()
        print(contenido)
        self.archivo.close()


r1=Register('fichero.txt')
r1.openFile()
r1.guardarInfo('esta es nueva info')
r1.mostrar()


## mediante un api seleccionar que info que queremos guardar