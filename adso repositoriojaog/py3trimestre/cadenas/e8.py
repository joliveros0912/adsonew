#Invente un cifrado de texto tipo murcielago o César. Puede utilizar alguna formula matemática para este fin. 9

def cifrado(cadena):
    cadena.lower()
    codigo=['c','a','n','c','i','o','e','s']
    print("canciones")
    print("012345678")
    s=''
    for i in range(len(cadena)):
        if cadena[i] in codigo:
            s+=str(codigo.index(cadena[i]))
        else:
            s+=cadena[i]
    print(s)
    
    
cadena=input('ingrese un texto :')
cifrado(cadena)