import random
r=round(random.randint(2,5))
"""lst=[[] for i in range(r)]             #forma1
print(lst)
for i in lst:
    for j in range(r):
        i.append(round(random.random()*100))
print(lst)"""
lista=[[round(random.random()*100)for i in range(r)] for i in range(r)]
print(lista)

#escriba una funcion que determine si un numero es positivo negativo o cero