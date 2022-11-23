dic ={
    'gato':'cat',                     #diccionariio
    'perro':'dog',
    'vaca':'crow',
    'caballo':'horse',
}
#sported()
print(dic)
print(sorted(dic))  #sirve para organizar el diccionario por las claves
print(sorted(dic.values())) #ordena por valores
print(sorted(dic.items())) #ordena en tuplas

print(dic.get('perro')) #muestra el valor de la clave
print(dic['vaca'])           #otra forma de imprimir el valor de la clave

del dic['perro'] #para eliminar---elimina clave y valor
print(dic)

dic['raton']='mouse' #para agregar clave y valor
print(dic)

dic.update({'perro':'dog'})  #agregar tambien
print(dic)

dic.popitem()  #elimina ultimo clave y valor
print(dic)

for i in dic.keys():  #recorre las claves
    print(i)

for i in dic.values(): #recorre los valores
    print(i)

for k,v in dic.items():     #muestra clave y valor por separado
    print(k,'->',v)

for items in dic.items(): #muestra clave y valor en tuplas
    print(items)