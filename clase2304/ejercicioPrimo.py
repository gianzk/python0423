numero=int(input("ingrese numero"))
es_primo =True

# Busco divisores en el rango de [2; numero-1]
for num in range(2, numero):
    if numero % num == 0:
        es_primo=False
        break # 

if es_primo:
    print("numero es primo")
else:
    print("numero no es primo")
# 8  => 1,2 
# 7  => 1,2,3,4,5,6,7