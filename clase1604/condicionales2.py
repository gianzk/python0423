msg="""
    # Ingrese una opcion 
    1.SUMAR
    2.RESTAR
"""
print(msg)

numero1=float(input("ingrese un numero"))
numero2=float(input("ingrese un numero"))
operacion=input("ingrse su operacion")

if operacion=='1':
    print('el resultado es ',numero1+numero2)
elif operacion=='2':
    print('el resultado es ',numero1+numero2)
else:
    print("ingrese una opcion correcta")


