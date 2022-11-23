"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. 
Llene la lista con números aleatorios. Encuentre la suma y el promedio de los números de la lista"""
import random

vector=[int(random.random()*100)for i in range(random.randint(10,25))]
print("lista:",vector)
sma=0
for i in vector:
    sma+=i
p=sma//len(vector)
print("la suma de los numeros de la lista es:",sma,"y el promedio es",sma//len(vector))