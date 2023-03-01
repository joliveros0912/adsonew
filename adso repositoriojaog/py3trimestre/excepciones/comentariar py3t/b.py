values = (1, 0)                                         #se crea una tupla
#x,y=10,12                                              #sele asignan variables a la tupla 
#print(divmod(10,1))                                    #imprime las veces que se puede dividir el primer numero ante el segundo 
try:                                                    #se pone a prueba el bloque de codigo dentro del  try
    q, r = divmod(*values)                              #se le asignan valores a las variables los cuales serian el resultado de las veces que se puede dividir el primer numero ante el segundo 
    print('valor de q=',q)                              #se imprime el valor de q
    print(f'q={q}')                                     #emprime el valor de q en la cadena recordando que se debe poner aal inicio una f
    print(f'r={r}')                                     #emprime el valor de r en la cadena recordando que se debe poner aal inicio una f
except (ZeroDivisionError, TypeError) as e:             #se estabalece una exceocion de doble error los cuales se les asigna el nombre e 
    print(type(e), e)                                   #se imprime el nombre del error que se esta presentando
    