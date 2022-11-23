"impares supermercado"
"ageragar productos, no hace calculos multiplicados por ejemplo si son 3 de arroz hacer arroz, arroz arroz, ademas del"
"promedio mostrar cual es el mas alto y cual es el mas bajo"
productos = {}

while True:
    name = input("Ingresa el nombre del producto: ")
    if name == '':
        break

    score = int(input("igrese el valor del producto: "))

    if name in productos:
        productos[name] += (score,)
    else:
        productos[name] = (score,)
l=[]
for name in sorted(productos.keys()):
    adding = 0
    counter = 0
    for score in productos[name]:
        adding += score
        counter += 1
    print(name, ": $", adding)
    print('el promedio del producto',name,'es de: $', adding//counter)
    ñ=adding//counter
    l.append(ñ)
print('el promedio del valor mayor es de: $',max(l))
print('el promedio de valor minimo es de: $',min(l))
