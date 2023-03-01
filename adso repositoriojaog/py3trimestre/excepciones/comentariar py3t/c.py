def try_syntax(numerator, denominator):                              #se crea una funcion con dos parametros 
    try:                                                             ##se pone a prueba el bloque de codigo dentro del  try
        print(f'In the try block: {numerator}/{denominator}')        #se imprime el resultado del numerador y el denominador dentro de la cadena teniendo en cuenta quese agrega la f antes de inicir la cadena 
        #quiero ver el resultado de la operacion en el print         #
        result = numerator / denominator                             #resultado de la division
    except ZeroDivisionError as zde:                                 #exceocion ZeroDivisionError con el nombre zde por si el denominador es 0 imprime esta
        print(zde)                                                   #
    else:                                                            #se establece un else 
        print('The result is:', result)                              # este imprime el resultado
        return result                                                # se crea un return el cual retorna el resultado de la division pero en la ejecucuon va aa mostrarse de ultimo lugar
    finally:                                                         # se establece un finaly en el cual se le dara salida 
        print('Exiting')                                             #imprime salida 
        #return "Fallo por zero"                                     #
#print(try_syntax(12, 4))                                            #
print(try_syntax(11, 5))                                             #se llama la funcion con un print 