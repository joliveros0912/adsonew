import random
sum=0

l=[int(random.random()*100)for i in range(random.randint(10,25))]
l=tuple(l)
print(l)
for i in l:
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