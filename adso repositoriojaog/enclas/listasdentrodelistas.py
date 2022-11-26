import random
lista=[[1,2,3], [3,2,1], [9,8,6]]
print(lista[1][1])
for i in range(3):
    for j in range(3):
        print(lista[i][j],end="-")
print(lista)


#comprension
lista=[i for i in range(10)]
print(lista)


import random
lista=[round(random.random()*100)for i in range(10)]
print(lista)

impar=[x for x in lista if x%2!=0]
print(impar)

par=[x for x in lista if x%2==0]
print(par)

parimpar=[0 if x%2==0 else x for x in lista]
print(parimpar)



board = []
for i in range(5):
    #row = [[] for i in range(3)]
    board.append([])
print(board)

board = [[] for i in range (3)]
print(board)


board = [[] for i in range (10)]
print(board)


board = [[] for i in range (10)]
print(board)