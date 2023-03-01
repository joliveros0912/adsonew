def numerosproi():
    try: 
        a=int(input("ponga: "))
        ae =[2001,9,11,777,666]
        if a in ae:
            print(a, "esta prohibido en mi sistema")
        elif a not in ae:
            print("usted dijito",a)
    except ValueError:
    #except UnboundLocalError:
        print("no admito  ese valor")
    #except ValueError:
    except UnboundLocalError:
        print("me perdi")

#numerosproi()

def sancocho():
    try:
        a=int(input('sancocho :'))
        lstSancocho=['agua','papa','yuca','pollo','arracacha','platano','silantro','aji(opcional)','pola para compañia','y si tiene plata echele mas']
        print(lstSancocho[a])
    except IndexError:
        print("no hay olla pal sancocho")
    except ValueError:
        print('sancocho sin papá')

#sancocho()


def edad ():
    
    a=int(input("ponga numero"))
    
    assert a>0," usted no a nacido"
    print("aq")
edad()

def excepcion1():
    try:
        arc = open("archivo.txt")
    except FileNotFoundError:
        print("Ese archivo no esta :c")

#excepcion1()



#excepcion2()

def excepcion3(x):
    try:
        print(x)
    except NameError:
        print("Socio no entiendo que es x")


#excepcion3()