""" nombre="gian"
edad =22
typeDocument="DNI"
"""
edad=int(input("ingrese una edad: "))
typeDocument=input("ingrese su tipo de documento:")
nombre=input("ingrese el nombre: ")
accesoPermitido=False 
if edad>=21 :
    print("es mayor de eddad")
    if typeDocument.upper()=="DNI":
        print("type document DNI")
        accesoPermitido=True
    else:
        print("tiene un documento no permitido")
elif edad==20:
    print("podemos evaluarte")
    if typeDocument.upper()!="PASPORT":
        print("si cumple con la evaluacion")
        accesoPermitido=True
else:
    print("es menor de edad")


if accesoPermitido:
    print(f"{nombre} ,tiene acceso permitido")
else:
    print(f"{nombre},no tiene acceso permitod")

print("esto siempre se ejecuta")

    