try:                                                       #se pone a prueba el bloque de codigo dentro del  try
    #print(1/1))
    raise SyntaxError                                      #se forza un syntax error 
except SyntaxError as e:                                   #si ocurre un sytax error se renombra a 'a' 
    print(e)                                               #imprime el nombre del error si ocurre de lo contrario umprimira un valor nulo o none 
    print('Cierra el parentesis')                          #imprime 
    
try:                                                       #se pone a prueba el bloque de codigo dentro del  try
    #raise ZeroDivisionError                               #
    print(1/0)                                             #pide imprimir el valor de la divicion
#except (ZeroDivisionError) as e:                          #
except ZeroDivisionError as zde:                           #si ocurre un error con la divicion por cero estara la excepcion ZeroDivisionError y esta se renombro a zde
    print(zde)                                             #se imprime el nombre de la excepcion
    #print('prueba error')                                 #