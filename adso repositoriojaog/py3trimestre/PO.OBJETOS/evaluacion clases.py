class pedido:
    def __init__(self,T_mat,C_mat):
        self.T_mat=T_mat
        self.__C_mat=C_mat
        
    def reservar(self,t_mat,c_mat):
        f=input('ingrese la fecha de reserva')
        material.reservar(self,f)
    def entregar():
        return

        
        
class lector:
    def __init__(self,id_usuario,nombre,direccion,telefono):
        self.__idUsuario=id_usuario
        self.nombre=nombre
        self.direccion=direccion 
        self.telefono=telefono 
        
    def reservar():
        return 
    def entregar():
        return 
        
class usuario:
    def __init__(self,codigo):
        self.codigoU=codigo
        self.__usuario={1:'estudiante', 2:'docente', 3:'natural'}
        
        
class material:
    def __init__(self,titulo,codigo,categoria,autor,edicion,estado):
        self.titulo=titulo
        self.codigo=codigo
        self.categoria=categoria
        self.autor=autor
        self.edicion=edicion
        self.estado=estado
        self.mat={}
        self.mat={'oso':{'codigo':11, 'categoria': 'infantil', 'autor': 'joel', 'estado': estado}}
    def consultarE(self,titulo):
        for a in (self.mat.values()):
            print(a)
        
    def reservar(self,fecha_reserva):
        estado=fecha_reserva
        self.mat.update({'oso':{'tipo':'comedia', 'categoria': 'infantil', 'autor': 'joel', 'estado': estado}})
        return self.mat 
        
    def entregar(self,entregado):
        estado=entregado
        self.mat.update({'oso':{'tipo':'comedia', 'categoria': 'infantil', 'autor': 'joel', 'estado': estado}})
        return self.mat 

#mat={titulo:{'tipo':tipo, 'categoria': categoria, 'autor': autor, 'estado': estado}}
        
class bibliotecario:
    def __init__ (self,):
        return