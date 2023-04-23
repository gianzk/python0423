###  + - * / pow => 
### 100 + 99 + 98+ ..2+ 1 

def suman(n:int)->int:
    if n==1:
        return 1
    else:
        return n+suman(n-1)
    
print(suman(100))

### 
## buscar caso base 1
def factorial(n:int)->int:
    if n!=1:
        return n*factorial(n-1)
    else:
        return 1
    
print(factorial(5))
