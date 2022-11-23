"""6. Calcular el máximo de números positivos introducidos por teclado,
    sabiendo que metemos números hasta que introduzcamos uno negativo.
    El negativo no cuenta."""
def calcular(n):
    maximo=0
    cont=0
    while n>=0:
        n =int(input("Ingrese un número"))
        if n>=0:
            cont +=1
        if n>maximo:
            maximo=n
    if cont>0:
        print("De los",cont ,"números positivos que usted digito", "el número mas grande es:",maximo)
    else:
        return"No digito un número positivo, fin del programa"
n=int(input("cero para iniciar"))
print(calcular(n))