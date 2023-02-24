values = (1, 0)                                         #se crea una tupla
#x,y=10,12                                              #sele asignan variables a la tupla 
#print(divmod(10,1))                                    #imprime las veces que se puede dividir el primer numero ante el segundo 
try:                                                    #se pone a prueba el bloque de codigo dentro del  try
    q, r = divmod(*values)                              #
    print('valor de q=',q)                              #
    print(f'q={q}')                                     #
    print(f'r={r}')                                     #
except (ZeroDivisionError, TypeError) as e:             #
    print(type(e), e)                                   #