'De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.'

def QTcadena():
    cadena=input('ingrese una cadena')
    vocales='AEIOUaeiou'
    vocales_tld='ÁÉÍÓÚáéíóú'
    consonantes='bcdfghjklmnñpqrstvxyzBCDFGHJKLMNLPQRSTVXYZ'
    caracter="!#$%‰&()*+,-./-:;<<=>>?@-[\]^_`{|}~¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼¿ÂÃÄÅÆÇÌÍÎÏÐÑÒÔÕÖ×ØÙÚÛÜÝÞßâãäåæçêëîïðñôõö÷øûüýþÿ€≠≤≥√Ω↑↓←→↔№▲►▼◄■□▪▫●○◊"
    vocales=list(vocales)
    vocales_tld=list(vocales_tld)
    consonantes=list(consonantes)
    caracter=list(caracter)
    v=0
    vt=0
    c=0
    cr=0
    for i in cadena:
        if i in vocales:
            v+=1
        elif i in vocales_tld:
            vt+=1
        elif i in consonantes:
            c+=1
        elif i in caracter:
            cr+=1
        else:
            return 'la cadena ',cadena,' es un poco extraña y puede contener caracteres no reconocibles'
    print(' la cadena',cadena,'tiene',v,'vocales \n tiene',vt,'vocales con tilde \ntiene',c,'consonantes \ny tiene',cr,'caracteres especiales')

print(QTcadena())