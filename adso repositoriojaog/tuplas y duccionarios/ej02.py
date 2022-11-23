'''TODO SE DEBE RESOLVER CON FUNCIONES: acciones:diseñar una lista tipo spotify depuedo anexar artista y 
cancion pero cada cancion debe de tener genero y duracion
-buscar artista
-buscar cancion
-eliminar artista
-ordenar alfabeticamente
-elque tiene mas canciones
-el que tiene la cancion mas larga
-el que tiene la cancion mas corta'''

spotify={}

def artista(spotify):
    ar=input('ingrese el nombre del artista:')
    gen=input('ingrese el genero:')
    can=input('ingrese  la cancion del artista:')
    dur=float(input('ingrese la duracion de la cancion en m/s'))
    spotify.update({ar:{'genero':gen,
                        'cancion':[can,dur, '\n']}})
    return spotify

def aggCancion(spotify):
    ar=input('ingrese el nombre del artista:')
    can=input('ingrese  la cancion del artista:')
    dur=float(input('ingrese la duracion de la cancion en m/s'))
    if ar in spotify:
        spotify.update({ar:{'cancion':[can,dur, '\n']}})
        return spotify
    
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
                exit()
        else:
            return
def todas(spotify):
    artista(spotify)
    aggCancion(spotify)
    buscarArts(spotify)
    
print(todas(spotify))
