def orden(x,y):
    if x<y:
        return "ascendente"
    elif x>y:
        return "descendente"
    else:
        return "iguales"
"""x=int(input("num x"))
y=int(input("num y"))"""
#print(orden(x,y))

import random
for i in range(10):
    x=(random.randrange(100))
    y=(random.randrange(100))
    print(x,"-" ,y,"estan en orden==",orden(x,y))