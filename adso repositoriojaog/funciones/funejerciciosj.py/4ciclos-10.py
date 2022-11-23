# Algoritmo para hallar el m.c.d de dos números m y n por el algoritmo de Euclides.

def hallar(n1,n2):
    restro=1
    while restro !=0:
        resto = n1 % n2
        if resto ==0:
            return"El M.C.D de los 2 números es: ",n2
        else:
            n1=n2
            n2 = resto
n1=int(input("Ingrese el número 1:   "))
n2=int(input("Ingrese el número 2:   "))
print(hallar(n1,n2))
