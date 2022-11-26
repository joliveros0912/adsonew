# Matriz (array, arreglo)
# Es una coleccion o conjunto de elementos formados
#Por filas y columnas 
# Matriz unidimensional (6) - vertical
for i in range(1,7):
    print(i)

print("\n")

#Matriz unidimencional (6) - horizontal 
for i in range(1,7):
    print(i, end = " ")

print("\n")

#Matriz bidimensional (6 x 6)
#For anidado
for i in range(1,7):
    for j in range(1,7):
        print(0, end="  ")
    print("")

#Ejemplo numero 2 
for i in range(1,7):
    for j in range(1,7):
        print(f"({i},{j})", end =" ")
    print("")

#Ejercisio: colocar 1 en la diagonal

for i in range(1,7):
    for j in range(1,7):
        if(i==j):
            print(1,end =" ")
        else:
            print(0,end =" " )
    print("  ")



my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
mi_lista = []
for i in my_list:
    if i not in mi_lista:
        mi_lista.append(i)
print(my_list)
print(mi_lista)


mi_lista = [1, 3, 5, 8, 10]
mi_lista2 = []
for i in mi_lista2:
    if i not in mi_lista2:
     mi_lista2.append(i)
print(mi_lista)
print(mi_lista2)


any_one = ["carlos", "diana", "pablo", "luis", "pablo"]
any_one2 = []
for i in any_one:
    if i not in any_one2:
        any_one2.append(i)
print(any_one)
print(any_one2)

