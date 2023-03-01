class Persona:                                                  # se crea la clase persona
    def __init__(self,nombre):                                  # se crea el constructor y se le dan parametros
        self.__nombre=nombre                                    # se referencia al objeto
        #print('Constructor Activado')                          #

    def getNombre(self):                                       # se crea esta funcion para ver el nombre
        return self.__nombre

    def setNombre(self,nombre):                                 # se crea esta funcion para cambiar el nombre
        self.__nombre=nombre

ob=Persona('Maria')                                             #se le asigna una variable a la clase y se le da un parametro en este caso 'maria'
print(ob.getNombre())                                           #se pife imprimir por medio del getter el nombre
ob.setNombre('Ana')                                             #por medio del setter se le cambia el nombre 
print(ob.getNombre())                                           # se solicita de nuevo el nombre
#print(type(ob))


tarea='agregar a la persona atributo documento hacerle getter y setter'
'hacer metodo para ver todos los datos pero debe estar en aprendiz'