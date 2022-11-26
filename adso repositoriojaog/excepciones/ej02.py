
def diaS(nd):
    try:
        nd=int(nd)
        if nd<=0:
            print('el numero no se encuentra en el rango')
            exit()
        dias=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
        nd=int(nd)
        print(dias[nd-1])
    except IndexError:
        print('el numero ingresado esta fuera del rango')
    except ValueError:
        print('debe ingresar un numero entero')

nd=input('ingrese un numero de 1 a 7 : ')
diaS(nd)