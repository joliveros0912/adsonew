#forma1
def divisores(num):
    try:
        for i in range(num):
            if num%i==0:
                print(i,'es divisor')
    except:
        print('indeterminacion')

divisores(19)
print('el programa continua aqui ')
#form2

def divisores(num):

    for i in range(num):
        if num%i==0:
            print(i,'es divisor')
try:
    divisores(19)
except:
    print('fallo')
    print('el programa continua aqui ')

#forma3
def divisores(num):
    try:
        for i in range(num):
            if num%i==0:
                print(i,'es divisor')
    except ZeroDivisionError:
        print('indeterminacion')

divisores(19)
print('el programa continua aqui ')

#forma4
def divisores(num):
    try:
        for i in range(num):
            if num%i==0:
                print(i,'es divisor')
    except ZeroDivisionError:
        print('indeterminacion')
    except TypeError:
        print('indeterminacion')
    except:
        print('toma la generica')

divisores('a')
print('el programa continua aqui ')

#forma5