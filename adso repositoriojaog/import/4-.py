"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios.
Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)"""
import random 
vec=[]
r=random.randint(10,25) 
for i in range(r):
    vec.insert(i,round(random.random()*100))
print("lista",vec)
n=len(vec)
for i in range(n-1):
    for j in range(n-1-i):
        if vec[j] > vec[j+1]:
                vec[j], vec[j+1] = vec[j+1], vec[j]
print("arreglo de menor a mayor",vec)
n=len(vec)
for i in range(n-1):
    for j in range(n-1-i):
        if vec[j] < vec[j+1]:
                vec[j], vec[j+1] = vec[j+1], vec[j]
print("arreglo de mayor a menor",vec)