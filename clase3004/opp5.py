

TYPES_PERSON=['NATURAL','JURIDICA']

class Persona:
    def __init__(self,fullname:str,tipo:str,documento,activo:bool=False):
            self.fullname=fullname
            self.tipo=tipo
            self.documento=documento
            self.activo=activo
            self.igv=18

    def __str__(self) -> str:
          return f"el impuesto es {self.igv}"
    
    def define_igv(self):
          if self.tipo.upper()!='NATURAL':
                self.igv+=5



tipoPersona=input("ingrese el tipo de la persona")
if tipoPersona.upper() in TYPES_PERSON:  
    p1=Persona('phil',tipoPersona,'8746645',True)
    p1.define_igv()
    print(p1)
else:
      print("ingrese un tipo valido")

