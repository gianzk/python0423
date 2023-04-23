# paso por valor 

a=4

def inc(x):
    a=x+4
    return a
c=inc(a) # paso por valor , porque solo registra una copia del valor


print(c)
print(a)


# Valor pasado por valor. Este genera una copia al valor pasado para no alterar el valor original del dato
def bar(x):
    x = x + 90 
    #print('valor de x dentro de la funcion "bar" es ', x)
    return x

x = 3 
bar(x)
print('valor de x a nivel global es ', x,"=>",bar(x))

# Valor puede
def foo(x : list):
    x[0] = x[0] * 99

# lista original
my_list = [1, 2, 3] 

foo(my_list)

# valor de variable global 'x' se mantiene
x = 7 

def foov2():   
    x = 42
    print(x)

    
#  llamo a la funcion
foov2()
print(x)

def foov3():
    global x
    x = 42 # reasignacion total x
    print('valor de x final', x)
    return x
    
# llamo a la funcion

x = 7
foov3()
print(x)
