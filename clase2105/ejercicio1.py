import pandas as pd

lista = [
            ["Rick", "Sanchez", 60],
            ["Morty", "Smith", 14]
        ]

df=pd.DataFrame(lista,columns=["nombre","apellido","edad"])
print(df)



