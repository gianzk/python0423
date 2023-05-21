import requests

def getDolar(tipoAccion,monto): 
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)
    data=response.json()
    compra=data['compra']
    venta=data['venta']
    if tipoAccion.upper()=='COMPRA':
        return f'tu monto {monto} equivale a {monto/compra}'
    if tipoAccion.upper()=='VENTA':     
        return f'tu monto {monto} equivale a {monto*venta}'   
print(getDolar('venta',100))

## Si tengo 20 dolares cuantos soles son

