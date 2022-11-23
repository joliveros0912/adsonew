"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. 
Llene la lista con números aleatorios. Encuentre la suma y el promedio de los números de la lista"""
import random
vec=[]
suma=0
cont=0
r=random.randint(10,25)
for i in range(r):
    vec.insert(i,round(random.random()*100))
    cont+=1
    suma+=vec [i]
print("lista:",vec)
print("la lista contiene la siguiente cantidad de numeros",cont)
print("la suma de los numeros de la lista es:",suma)
prom=suma//cont
print("el promedio de los numeros de la lista es:",prom)