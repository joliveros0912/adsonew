import os

spotify={} 
def aggcan(spotify):
    can=input('Escriba el nombre de la cancion: ')
    spotify.update({can:{}}) 
    return spotify

def detallesCan(spotify): 
    can=input('Escriba el nombre de la cancion: ')
    if can not in spotify: 
        print('No se encuentra la cancion en spotify') 
        return spotify
    ar=input('Escriba el nombre del artista: ') 
    gen=input('Escriba el genero musical: ')
    dur=input('Escriba la duracion de la cancion: ')

    if can in spotify: 
        spotify.update({can:{'artista':ar,'genero':gen,'duracion':dur}}) 
    return spotify
    
def busArt(spotify): 
    bus=input('¿Que artista desea buscar?: ') 
    for a in (spotify.values()): 
        if bus==a['artista']: 
            print('El artista',bus,'se encuentra en spotify y su genero es:',a['genero']) 
            return None 
    print('El artista no se encuentra, ingrese la cancion con el artista') 
    
def busCan(spotify): 
    bus=input('¿Que cancion desea buscar?: ') 
    for i in sorted(spotify.keys()): 
        if bus==i:
            print('La cancion',bus,'se encuentra en spotify') 
            return None 
    print('La cancion no se encuentra en spotify') 

def eliCan(spotify): 
    bus=input('¿Que cancion desde elminiar?: ') 
    for i in sorted(spotify.keys()): 
        if bus==i: 
            del spotify[i] 
            print('La cancion',bus,'fue eliminada correctamente') 
            return None 
    print('La cancion no se encuentra, ingrese el nombre primero') 
    
def mayor(spotify): 
    mayor=dict 
    mayor_valor=0 
    for a in (spotify.keys()): 
        minutos=spotify[a]['duracion'][0] 
        minutos+=spotify[a]['duracion'][1] 
        segundos=spotify[a]['duracion'][3] 
        segundos+=spotify[a]['duracion'][4]
        segundos= int(segundos)+int(minutos)*60 
        if mayor_valor<=segundos: 
            mayor_valor=segundos 
            mayor=a 


    print('La cancion mas larga es',mayor) 
        
def menor(spotify): 
    menor=dict 
    menor_valor=9e99999 
    for a in (spotify.keys()): 
        minutos=spotify[a]['duracion'][0] 
        minutos+=spotify[a]['duracion'][1] 
        segundos=spotify[a]['duracion'][3] 
        segundos+=spotify[a]['duracion'][4] 
        segundos= int(segundos)+int(minutos)*60 
        if menor_valor>=segundos: 
            menor_valor=segundos 
            menor=a 

    print('La cancion mas corta es',menor) 

while True: 
    os.system ("cls")
    pedir=int(input('Bienvenido al menu \n Presione 1 para agregar una cancion \n Presione 2 para agregar informacion detallada a una cancion ya agregada \n Presione 3 para buscar un artista \n Preione 4 para buscar una cancion \n Presione 5 para eliminar una cancion \n Presione 6 para mostrar todo lo agregado \n Presione 7 para mostrar la cancion mas larga \n Presione 8 para mostrar la cancion mas corta \n Presione 9 para finalizar el programa: '))

    if pedir==1: 
        (aggcan(spotify)) 
        print(spotify)
    elif pedir==2: 
        (detallesCan(spotify)) 
        print(spotify)
    elif pedir==3: 
        (busArt(spotify)) 
        print(spotify)
    elif pedir==4:
        (busCan(spotify)) 
        print(spotify)
    elif pedir==5: 
        (eliCan(spotify)) 
        print(spotify)
    elif pedir==6: 
        print('Todas las canciones con su informacion respectiva agregada son las siguientes:',spotify) 
    elif pedir==7: 
        mayor(spotify)
    elif pedir==8: 
        menor(spotify) 
    elif pedir==9: 
        break 
    else:
        print('El numero no es valido')
    os.system('pause')