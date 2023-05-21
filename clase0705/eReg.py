import re

texto = "En esta cadena se encuentra una palabra mágica"
re.search('mágica', texto)


def validtNumber(numero):
    patron=r'^9\d{8}$'
    a=re.match(patron,numero)
    print(a,a.start()-a.end())
    
validtNumber('95145')
