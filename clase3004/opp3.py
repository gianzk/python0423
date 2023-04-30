### principios encapsulacion , herencia , poliformismo , sobrecarga
# clase padre o base
class Figura:
    def __init__(self,lados):
        self.lados=lados
        self.area=0
        self.name="name"
    def __str__(self):
        return f"esta figura tiene {self.lados} lados"

#clase hija o heredada
class Cuadrado(Figura):

    def __init__(self,lados):
        super().__init__(lados)
    def area(self,base,altura):
        return base*altura
    def __str__(self):
        return f"es un cuadrado"
class Triangulo(Figura):
    def __init__(self,lados):
        super().__init__(lados)
    def area(self,base,altura):
        return base*altura/2
    
c1=Cuadrado(4)
print(c1.area)
t1=Triangulo(3)
print(t1)
print(c1)