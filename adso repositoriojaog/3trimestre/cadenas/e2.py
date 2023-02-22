'pida una cadena por teclado y diga cual es su valor al sumar sus codigos'
#cual es su valor numerico de acuerdo a los codigos del alfabeto

cadena=input('ingrese una cadena de texto :')
def valortexto(cadena):
    acu=0
    for i in cadena:
        c=ord(i)
        acu+=c
    print('el valor de los codigos de la palabra', cadena,'es de :',acu)

valortexto(cadena)