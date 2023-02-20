'solicite una cadena e imprimala en todas las formas posibles en cuanto a mayusculas y minusculas'

def MayuMinu(cadena):
    print('cadena con inicial mayuscula :',cadena.capitalize())
    print('cadena en mayuscula :',cadena.upper())
    print('cadena en minuscula :',cadena.lower())
    
    
cadena=input('ingrese una cadena :')
MayuMinu(cadena)