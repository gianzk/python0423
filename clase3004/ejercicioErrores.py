def fxWithError():
    m = int(input("Introduce un número: "))
    n = 7
    print("{}/{} = {}".format(n,m,n/m))

def fxWithoutError():
    try:
        m = int(input("Introduce un número: "))
        n = 7
        print("{}/{} = {}".format(n,m,n/m))   
    except:
        print("hubo un error ")   

#fxWithoutError()
""" 
try:
    m = int(input("Introduce un número: "))
    n = 7
    print("{}/{} = {}".format(n,m,n/m))   
except:
    print("hubo un error <ejectuando desde el archivo principal ")   
 """

def fxWithoutErrorV2(lista):
    try:
        lista.pop()
    except:
        print("No existe elementos el try fallo")  
    else: 
        print("estos son los elementos que quedan el try fue correcto",lista)

#fxWithoutErrorV2([]) # sin erroes fxWithoutErrorV2([1,2,3,4])


def fxWithoutErrorV3():
    try:
        m = int(input("Introduce un número: "))
        n = 7
        resultado=n/m
    except:
        print("hubo un error ")   
    else:
        print(resultado)   
    finally:
        print("fin de la iteracion")

#fxWithoutErrorV3()


def fx1(lista2):
    flag=False
    values=0
    try:
        flag=False
        values=0
        lista2.pop()
    except:
        print("hubo un error")
        flag=True
        values=0
    else:
        values=1
    finally:
        fx2(flag,values)

def fx2(flag,values):
    if flag:
        print("hubo errores en la anterior ejecucion ",values)
    else:
        print("no hubo errores",values)
    
fx1([]) # sin errores fx1([1,2,3])
    
### que pasa si escribo bastantes lineas incluso lo divido en funciones pero falla y no se de que falla ?

def fxWithoutErrorV4(m,n):
    try:
        t=(1,2,3)
        t[1]=2
        a=0
    except Exception as mesageError:
        print("hubo un error",mesageError)
    else:
        print("el resultado correcto es",a)
    finally:
        print("termino la funcion")

#fxWithoutErrorV4(1,0)