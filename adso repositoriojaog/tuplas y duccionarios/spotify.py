'''TODO SE DEBE RESOLVER CON FUNCIONES: acciones:diseñar una lista tipo spotify depuedo anexar artista y 
cancion pero cada cancion debe de tener genero y duracion
-buscar artista
-buscar cancion
-eliminar cancion
-ordenar alfabeticamente
-elque tiene mas canciones
-el que tiene la cancion mas larga
-el que tiene la cancion mas corta'''

from platform import java_ver


spotify={}

def artista(spotify):

    ar=input('ingrese el nombre del artista:')
    spotify.update({ar:[]})
    print(spotify)
    return spotify

def aggCancion(spotify):
    ar=input('ingrese el nombre del artista:')
    if ar in spotify.keys():
        can=input('ingrese  la cancion del artista:')
        gen=input('ingrese el genero:')
        dur=input('ingrese la duracion de la cancion en m/s')
        spotify[ar].append[{'cancion':can,
                            'genero':gen,
                            'duracion': dur}]
        print(spotify)
    else:
        print('el artista no se encuentra en spotify')

def buscarArts(spotify):
    buscar=input('¿Qué artista desea buscar')
    for i in sorted(spotify.keys()):
        if buscar==i:
            print('el artista buscado se encuentra en la lista')
        else:
            print('el artista',buscar,'no se encuentra en la lista de canciones spotify')

    while True:
        print(spotify)
        pedir=int(input('si desea agregar una cancion a este artista marque 1, de lo contrario precione 0'))
        if pedir==1:
            aggCancion(spotify)
            p=int(input('si desea agregar una cancion marque 1, si desea salir marque cero'))
            if p==0:
                break
        else:
            break

print(spotify)

def eliminar(spotify):
    e=input('que cancion desea eliminar')
    for i in sorted(spotify.keys()):
        if e==i:
            del spotify[i]
            print('la cancion',e,'fue eliminada con exito')
            return None
        else:
            print('la Cancion no se encuentra en spotify')
            return None

def bcancion(spotify):
    bs=input('que cancion desea buscar')
    for i in sorted(spotify.values()):
        if bs in i:
            print('la cancion',bs,'si se encuentra en spotify')
            return None
        else:
            print('la cancion no se encuentra en spotify')
            return None




def todas(spotify):
    artista(spotify)
    aggCancion(spotify)
    #buscarArts(spotify)
    #eliminar(spotify)
    #bcancion(spotify)
print(todas(spotify))
import os
#while True:
    #os.system ("cls")
   # pedir=int(input('Bienvenido al menu \n Presione 1 para agregar una cancion \n Presione 2 para agregar informacion detallada a una cancion ya agregada \n Presione 3 para buscar un artista \n Preione 4 para buscar una cancion \n Presione 5 para eliminar una cancion \n Presione 6 para mostrar todo lo agregado \n Presione 7 para mostrar la cancion mas larga \n Presione 8 para mostrar la cancion mas corta \n Presione 9 para finalizar el programa: '))
    #if pedir==1:
    #    (aggCancion(spotify))
   # elif pedir==2:
   #     (buscarArts(spotify))
   # elif pedir==3:
   #     (bcancion(spotify))
   # elif pedir==5: #Si pedir es igual a 5
   #     (eliminar(spotify)) #Funcion de eliminar una cancion
   # elif pedir==6: #Si pedir es igual a 6
   #     print('Todas las canciones con su informacion respectiva agregada son las siguientes:',spotify) #Imprime el diccionario
    #elif pedir==7:
   #     mayor(spotify)
   # elif pedir==8:
   #     menor(spotify)
  #  elif pedir==9:
    #    break
   # else:
   #     print('El numero no es valido') #Si no se inserta alguno de estos numeros, el programa saca este mensaje y vuelve a pedir
   # os.system('pause')
