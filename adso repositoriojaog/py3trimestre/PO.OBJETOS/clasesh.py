class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre
    
    def getDocumento(self):
        return self.__documento

    def setNombre(self,nombre):
        self.__nombre=nombre

    def setDocumento(self,documento):
        self.__documento=documento

#ob=Persona('joel','1003882456')
#print(ob.getNombre())
#print(ob.getDocumento())
#ob.setNombre('antonio')
#print(ob.getNombre())
#ob.setDocumento('12345')
#print(ob.getDocumento())
#print(type(ob))#
class Aprendiz(Persona):
    def __init__(self,nombre,documento,ficha):
        super().__init__(nombre,documento)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha
    
    def setficha(self,ficha):
        self.__ficha=ficha

ap=Aprendiz('joel','1003882456','adso')
#print(ap.getFicha())
#print(ap.setficha('antonio'))
print(ap.getNombre(),ap.getDocumento(),ap.getFicha())


tarea='agregar a la persona atributo documento hacerle getter y setter'
'hacer metodo para ver todos los datos pero debe estar en aprendiz'