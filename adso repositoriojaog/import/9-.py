"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. 
Llene la lista con números aleatorios.Encuentre la mediana de los números de la lista"""
import random

vec=[]
r=random.randint(10,25)
cont=0
suma=0
for i in range(r):
    vec.insert(i,round(random.random()*100))
    cont+=1
    suma+= vec [i]
print("lista",vec)
n=len(vec)
for i in range(n-1):
    for j in range(n-1-i):
        if vec[j] > vec[j+1]:
                vec[j], vec[j+1] = vec[j+1], vec[j]
print("lista menor a mayor",vec)
pm=cont//2
print("la mediana de la lista es:",vec [pm])
