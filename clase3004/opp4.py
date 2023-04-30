## crear un clase venta , para que inicie una venta debe ya definir que se vaya a realizar pero con status 
# aun por pagar
##que tenga el init y el str de la venta 
## y un metodo de pagar que es simplemte cambiar el status pagado a no pago


class Venta:
    def __init__(self,producto,monto) -> None:
        self.producto=producto
        self.monto=monto
        self.porPagar=False
    def __str__(self) -> str:
        if self.porPagar:
            status=" esta pagado"
        else:
            status=" esta por pagar"
        return f"la venta {self.producto} es de monto {self.monto} {status}"    
    def pagar(self):
        self.porPagar=True


while True:
    v1=Venta("p1",100)
    print(v1)
    v1.pagar()
    print(v1)
