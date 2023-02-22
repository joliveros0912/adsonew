def ClaveValor(dic):
    if dic=="":
        print("vacio")
    else:
        for k,v in dic.items():     
            print(k,'->',v)


def Add(clave,valor,dic):
    if clave=="":
        print("vacio")
    elif valor=="":
        print("vacio")
    elif dic=="":
        print("vacio")
    else:
        dic[clave]=valor
        print(dic)
    
    
def ResulClave (clave,dic):
    if clave=="":
        print("vacio")
    elif dic=="":
        print("vacio")
    else:
        print(dic.get(clave)) 

def eliminar (dic,clave):
    if clave=="":
        print("vacio")
    elif dic=="":
        print("vacio")
    else:
        del dic[clave] 
        print(dic)

def CuantosValores (dic):
    if dic=="":
        print("vacio")
    else:
        cont=0
        for i in dic.keys():
            Cont+=1
            return cont
