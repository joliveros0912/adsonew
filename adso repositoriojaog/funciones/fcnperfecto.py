def sumaDivisores(num):
    suma=0
    for i in range(1,num):
        if num%i==0:
            suma+=i
    return suma
def perfectos(num):
    sum=sumaDivisores(num)
    if sum==num:
        return "perfecto"
    else:
        return "no perfecto"
def primos(num):           #determina que num es primo
    sum=sumaDivisores(num)
    if sum==1:
        return "es primo"
    else:
        return "no es primo"

print(primos(6))