"""Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números aleatorios.
Encuentre la moda de los números de la lista"""
import random
vec=[]
r=random.randint(10,25)
listv=[]

for i in range(r):
    vec.insert(i,round(random.random()*100))
print("lista:",vec)
for i in range(len(vec)): 
    cont=0
    for j in vec:    
        if vec[i] == j:
            cont+=1 
    if cont!=0:
        listv.append(cont)
    else:
        listv.append(0)
print("cantidad de veces que se repiten los numeros de la lista:",listv)
mayor=0
pos=0
for i in range(len(vec)):
    if mayor<listv[i]:
       mayor=listv[i]
print('la cantidad que mas se repite un numero es:',mayor)
for j in range(len(listv)):
    if mayor==listv[j]:
        print('la moda es ',vec[j])