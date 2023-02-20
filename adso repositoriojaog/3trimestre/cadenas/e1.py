'cuantas letras del abecedario estan en la cadena, si estan repetidas cuentelas solo una vez'

def Cuantas(cadena):
    cont=0
    lst=[]
    for i in cadena:
        if i not in lst:
            lst.append(i)
            cont+=1
        else:
            None
    print(cont)

cadena=input('ingrese su cadena :')
Cuantas(cadena)