"""llene una lista con numeros aleatorios entre 10 y 25 elementos.llene la lista con numeros aleatorios.
sume los pares y saque promedio de los impares"""
import random
vec=[]
r=random.randint(10,25)
sumap=0
sumai=0
prom=0
for i in range(r):
    vec.insert(i,round(random.random()*100))
print("lista=",vec)
for i in range(len(vec)):
    if vec [i]%2==0:
        print(vec[i],"es par")
        sumap+=vec[i]
    else:
            print(vec [i]," es impar")
            prom+=1
            sumai+= vec [i]
print("la suma de los pares es=",sumap)
promedio=sumai//prom
print("el promedio de los impares es=",promedio)