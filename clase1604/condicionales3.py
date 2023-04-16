salario=float(input("ingrese tu salario"))
impuesto=0.0
"""
    menos 10k => 5%
    entre 10k y 20k => 15 %
    entre 20 y 35k =>20%
    entre 35 y 50k => 30%
    mas 50 k 45

"""
t=0.05
if salario < 10000:
    t = 0.05
elif salario >= 10000 and salario<20000:
    t = 0.15
elif salario >= 20000 and salario<35000:
    t = 0.20
elif salario >= 35000 and salario<60000:
    t = 0.30
else:
    t = 0.45

impuesto=salario*t
print(impuesto)