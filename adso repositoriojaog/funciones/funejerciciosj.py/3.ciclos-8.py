#8.	Determinar cuales son los múltiplos de 5 comprendidos entre 1 y N.
def determinador(n):
    mx=0
    for i in range(1,n+1):
        mx=5*i
        print("5 multiplicado por",i,"es igual =",mx)


n=int(input("Ingrese la cantidad de multiplos de 5 que desea conocer:"))
determinador(n)
