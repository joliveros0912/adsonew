"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. 
Llene la lista con números aleatorios.Encuentre la mediana de los números de la lista"""
import random
vector=[int(random.random()*100)for i in range(random.randint(10,25))]
print("lista:",vector)
n=len(vector)
for i in range(n-1):
    for j in range(n-1-i):
        if vector[j] > vector[j+1]:
                vector[j], vector[j+1] = vector[j+1], vector[j]
pm=len(vector)//2
print("lista menor a mayor=",vector,"\nla mediana de la lista es:",vector [pm])