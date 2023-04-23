"""
    1.etapa es definicion <=> def  , es como la maqueta 
    2.invocacion
"""

def sumar():
    a=int(input("ingrese numero"))
    b=int(input("ingrese numero"))
    print(a+b)

#sumar()

def sumarv2(num1,num2):
    print(num1+num2)

c=2
d=3
#sumarv2(c,d)

# return keyword
def sumarv3(num1,num2):
    return num2+num1

e=sumarv3(c,d)
print(e)


def bar(x=2):
    return x + 90

# my_var = 3
print(bar())
print(bar(3))

def indeterminados_posicion(*args):
    print(type(args))
    for arg in args:
        print(arg)

indeterminados_posicion(5,"Hola",{'dia':'sabado'})

### funciones anidadas
def paso1():
    print("paso 1")

def paso2():
    print("paso2")



def main():
    paso1()
    paso2()

main()


