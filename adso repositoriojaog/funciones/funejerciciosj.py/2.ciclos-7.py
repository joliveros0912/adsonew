"""7. Encontrar un número natural n más pequeño tal que la suma de los n
    primeros números naturales (1 + 2 + 3 + 4…..) exceda de una cantidad (máximo)
    introducida por el teclado.
    Es decir cuantos números  de la serie de los naturales debo sumar para superar el dato máximo."""
def encontrar(n):
    cont=0
    while cont*(cont+1)<=2*n:
        cont+=1
    return cont
n=int(input("Ingrese el número máximo   "))
print("El número natural mas pequeño que excede al dato es:",encontrar(n))