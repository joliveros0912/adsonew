""" Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Muestre cuales y cuantos son primos"""
import random
vec=[]
sum=0
r=random.randint(10,25)
for i in range(r):
    vec.insert(0,int(random.random()*100))
print("lista=",vec)
for i in vec:
    cont=0
    for j in range (1,i+1):
        if i % j == 0:
            cont+=1
    if cont==2:
        print(i,"es un numero primo")
        sum+=1
    else:
        print(i,"no es un numero primo")
print("la cantidad de numeros primos es=",sum)