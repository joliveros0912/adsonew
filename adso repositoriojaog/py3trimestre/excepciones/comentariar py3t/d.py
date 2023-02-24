def edad():                                                 #se crea una funcion llamada edad sin parrametros 
    try:                                                    #se pone a prueba el bloque de codigo dentro del  try
        tuedad=int(input("introduce tu edad"))              #se crea un input que recibira un valor numerico entero
        print(f'tu edad es  {tuedad}')                      #imprime el valor ingresado dentro de la cadena y se coloca antes de abrir la letra f 
        #print('Tu edad es ',tuedad)                        #
    except ValueError as e:                                 #se crea una excepcion ValueError con el nombre e
        print(e)                                            # imprime error de valor 
        print("La edad debe ser un valor numerico...")      #imprime 
        edad()                                              # llama de nuevo la funcion para inicie de nuevo
    
edad()                                                     #llama la funcion por primer vez