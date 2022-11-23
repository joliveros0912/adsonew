"""llene una lista con numeros aleatorios entre 10 y 25 elementos.llene la lista con numeros aleatorios.
sume los pares y saque promedio de los impares"""
import random

vector=[int(random.random()*100)for i in range(random.randint(10,25))]
print("lista:",vector)
suma1=0
suma2=0
pares=[x for x in vector if x%2==0]
impares=[x for x in vector if x%2!=0 ]
for i in pares:
    suma1+=i
for i in impares:
    suma2+=i
print("pares=",pares,"\nsuma de los pares=",suma1,"\nimpares=",impares,"\npromedio de los impares=",suma2//len(impares))