def sancocho():
    try:
        a=int(input('sancocho :'))
        lstSancocho=['agua','papa','yuca','pollo','arracacha','platano','silantro','aji(opcional)','pola para compañia','y si tiene plata echele mas']
        lstSancocho[a]
    except IndexError:
        print("olla muy pequeña pal sancocho")
    except ValueError:
        print('sancocho sin papá')
    else:
        print(lstSancocho[a])
    

#sancocho()




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
    else:
        numerosproi()

numerosproi()