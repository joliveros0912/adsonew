"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios.
Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que posiciones esta.
Si no está agréguelo al final de la lista."""
    
import random

vector=[int(random.random()*100)for i in range(random.randint(10,25))]
print("lista:",vector)
n=int(input("ingrese el numero que desea buscar"))
if n in vector:
    nv=[indice for indice, dato in enumerate(vector) if dato == n]
    print("el numero buscado se encuentra en la o las pociciones:",nv,"de la lista")
else:
    vector.append(n)
    print(n,"no se encuentra en la lista y sera agregado a continuacion \n lista con el numero agregado",vector)
