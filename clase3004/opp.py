#  variable nota => dict o lsit => class
#

#print(__name__) # objecto principal que se ejecuta


datosClientes=[]

class CatalogoClientes:
    def __init__(self):
        self.listClientes=[]

    def agregarCliente(self,cliente):
        self.listClientes.append(cliente)

class Cliente:
    def __init__(self,name,nroDocumento,phone,email):
        self.name=name
        self.nroDocumento=nroDocumento
        self.phone=phone
        self.email=email
        self.address=""
        self.orders=[]
        self.statusOrder=False

    def pedirOrden(self,order):
        self.orders.append(order)
        self.statusOrder=True
    def cancelarOrder(self,nroDocumento):
        if nroDocumento==self.nroDocumento:
            self.statusOrder=False
            self.orders=[]
        else:
            print("no puedes cancelar la orden")
    def mostrarOrder(self):
        for i in self.orders:
            print(i)
c1=Cliente('c1Name','564545','9764644','gamsdadsa@awdads.com')

c1.pedirOrden('product1')
c1.cancelarOrder('adsasdads')
c1.mostrarOrder()

datosClientes.append(c1)

c2=Cliente('c2Name','564545','9764644','gamsdadsa@awdads.com')

c2.pedirOrden('product2')
c2.cancelarOrder('adsasadads')

datosClientes.append(c2)

print(datosClientes)

class Producto:
    def __init__(self,id,name,price,stock):
        self.id=id
        self.name=name
        self.price=price
        self.stock=stock
    def __str__(self):
        return f"el producto se llama {self.name} con el precio de {self.price} y stock {self.stock}"


pr1=Producto(1,'celular',456,100)

print(pr1)