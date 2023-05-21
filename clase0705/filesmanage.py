texto = "Una linea con texto\nOtra linea con texto"
import os
print(os.getcwd())
# Ruta donde crearemos el fichero, w indica escritura (puntero al principio)
# De existir el archivo, este será eliminado y creado uno nuevo 
with open('./fichero.txt','w') as f:
    # Escribimos el texto
    f.write(texto) 

