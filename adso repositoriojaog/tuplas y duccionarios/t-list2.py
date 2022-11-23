from operator import contains
import random
sum=0
r=round(random.randint(5,10))
l=tuple(round(random.random()*100)for i in range(r))
print(l)
for i in l:
    cont=0
    for j in range(1,i):
        if i%j==0:
            cont+=1
    if cont == 1 :
            print(i,"es un numero primo")
            sum+=1
    else:
        print(i,"no es un numero primo")
print("la cantidad de numeros primos es=",sum)