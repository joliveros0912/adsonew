#escriba una funcion que determine si un numero es positivo negativo o cero
def determi(n):
    if n>1:
        print("positivo=",n)
    elif n==0:
        print("cero=",n)
    elif n<-1:
        print("negativo",n)
        
n=int(input("escriba el numero="))
determi(n)

