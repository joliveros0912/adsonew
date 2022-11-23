"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios.
Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que posiciones esta.
Si no está agréguelo al final de la lista."""
import random
vec=[]
cont=0
r=random.randint(10,25)
for i in range(r):
    vec.insert(i,round(random.random()*100))
print(vec)
n=int(input("que numero desea buscar"))
if n in vec:
    print(n,"se encuentra en la lista")
    nv=[indice for indice, dato in enumerate(vec) if dato == n]
    cont+=1
    print("se encuentra",cont,"veces")
    print("en las pocisiones",nv)
else:
    print(n,"no se encuentra en la lista y sera agregado a continuacion")
    vec.append(n)
    print(vec)