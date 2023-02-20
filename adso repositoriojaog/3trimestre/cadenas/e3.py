'cuantas veces se repite un caracter dado'

def caracRep(caracter):
    cont=0
    ls=[]
    for i in caracter:
        if i not in ls:
            ls.append(i)
        else:
            cont+=1
    return 'la cantidad de caracteres repetidos es :',cont



caracter=input('ingrese los caracteres  :')
print(caracRep(caracter))
