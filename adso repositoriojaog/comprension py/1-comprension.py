
import random

vector=[int(random.random()*100)for i in range(random.randint(10,25))]
suma=0
prom=0
print("lista",vector)
for i in range(len(vector)):
    suma+=vector[i]
    prom=suma//len(vector)
    if vector[i]==prom:
        print(vector[i],"es igual al promedio")
    elif vector[i]>prom:
        print(vector[i],"es mayor al promedio")
    elif vector [i]<prom:
        print(vector[i],"es menor al promedio")
print("la cantidad de numeros es",len(vector),"\n la suma de la lista",suma,"\npromedio de la lista es",prom)