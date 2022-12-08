#calcular el trabajo realizado por una persona que mueve una caja
#recorre una distancia de 15m
#esta cuerda forma un angulo de 30° con respecto a la horizontal o piso
#si la tension es de 6n    ¿cual es el trabajo realizado?


import math
a=30
b=6
e=15
z=math.radians(a)
c=math.cos(z)
print('el trabajo realizado es de',b*e*c,end=' j')