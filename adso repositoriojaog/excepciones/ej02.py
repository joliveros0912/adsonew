
lst=[]
def diaS(nd):
    try:
        nd=int(nd)
        if nd>=8:
            print('el numero no es valido')
            exit()
        if nd==1:
            return 'lunes'
        if nd==2:
            return 'martes'
        if nd==3:
            return 'miercoles'
        if nd==4:
            return 'jueves'
        if nd==5:
            return 'viernes'
        if nd==6:
            return 'sabado'
        if nd==7:
            return 'domingo'
    except ValueError:
        print('debe ingresar un numero ENTERO, EJECUTE NUEVAMENTE')
        exit()
while True:
    nd=input('ingrese un numero de 1 a 7 : ')
    z=diaS(nd)
    lst.append(z)
    print(lst)