## funciones string

my_string2 = "This string will,be,split"
print(my_string2.split(sep=","))

my_string = "Where's Waldo?"
print(my_string.find("Waldo"))


print(my_string.find("Wenda")) # No se encotro palabra buscada
if my_string.find("Wenda")==-1:
    print("no se encontro cadena")


my_string.index("Waldo")

my_string3 = "How many fruits do you have in your fruit basket?"
my_string3.count("fruit")

my_string4 = "The red house is between the blue house and the old house"
print(my_string4.replace("house", "car"))
