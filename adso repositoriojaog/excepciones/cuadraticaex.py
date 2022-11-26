
from math import sqrt
a=int(input('ingrese primer valor'))
b=int(input('ingrese segundo valor'))
x=int(input('ingrese tercer valor'))
def cuadratica(a,b,x):
    try:
        r1=  b+ sqrt(b**2 - 4*a*x) / (2*a)
        r2=  b- sqrt(b**2 - 4*a*x) / (2*a)
        print(r1)
        print(r2)
    except ZeroDivisionError:
        print('no se puede dividir por cero')
    except ValueError:
        print('No se puede realizar esta operacion')
    except:
        print('error fuera de lo comun')

cuadratica(a,b,x)