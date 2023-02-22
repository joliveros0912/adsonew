# # Demostración de la función ord ().
char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))



# Demostración de la función chr.
print(chr(97))
print(chr(945))


# Indexando cadenas.
the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()


# Iterando a través de una cadena.
the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()


# Rebanadas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])



# in and not in cadenas
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)


#Operaciones con cadenas: continuación
alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)


#Operaciones con cadenas: min()
# Demonstrando min() - Ejemplo 1:
print(min("aAbByYzZ"))

# Demonstrando min() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))


#Operaciones con cadenas: max()
# Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ"))

# Demostración de max() - Ejemplo 2 & 3:
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))


#Operaciones con cadenas: el método index()
# Demonstrando el método index():
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

#Operaciones con cadenas: la función list()
# Demostración de la función list():
print(list("abcabc"))

#Operaciones con cadenas: el método count()
# Demostración de la función list():
print("abcabc".count("b"))
print('abcabc'.count("d"))


# Las cadenas pueden ser concatenadas usando el operador +, y replicadas usando el operador *. Por ejemplo:
asterisk = '*'
plus = "+"
decoration = (asterisk + plus) * 4 + asterisk
print(decoration)


# Algunas otras funciones que se pueden aplicar a cadenas son:
list() â crea una lista que consta de todos los caracteres de la cadena.
max() â encuentra el carácter con el punto de código máximo.
min() â encuentra el carácter con el punto de código mínimo.


"METODOS EN CADENAS"

#El método capitalize()
# Demostración del método capitalize():
print('aBcD'.capitalize())

#El método center()
# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')  #genera una copia de la cadena original, tratando de centrarla dentro de un campo de un ancho especificado.
print('[' + 'gamma'.center(20, '*') + ']')


#El método endswith()
# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")     #comprueba sila cadena dada termina conel argumento especificado y devuelve True(verdadero) o False(falso),dependiendo del resultado
else:
    print("no")
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))


#El método find()
# Demostración del método find():
print("Eta".find("ta"))
print("Eta".find("mma"))
# es similar al método index(), el cual ya conoces - busca una subcadena y devuelve el índice de la primera aparición de esta subcadena, pero:
#Es más seguro, no genera un error para un argumento que contiene una subcadena inexistente (devuelve -1 en dicho caso).
#Funciona solo con cadenas - no intentes aplicarlo a ninguna otra secuencia.

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print('kappa'.find('a', 2))
#El segundo argumento especifica el índice en el que se iniciará la búsqueda (no tiene que estar dentro de la cadena).
#De las dos letras a, solo se encontrará la segunda. Ejecuta el código y verifica.


#El método isalnum()
# Demostración del método the isalnum():
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())         #comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) y devuelve True(verdadero)
print('@'.isalnum())          #o False(falso) de acuerdo al resultado.
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())


#El método isalpha()
# Ejemplo 1: Demostración del método isapha(): es más especializado, se interesa en letras solamente.
print("Moooo".isalpha())
print('Mu40'.isalpha())

#El método isdigit()
# Ejemplo 2: Demostración del método isdigit():  busca solo dígitos - cualquier otra cosa produce False(falso) como resultado.
print('2018'.isdigit())
print("Year2019".isdigit())


# Ejemplo 1: Demostración del método islower(): es una variante de isalpha() - solo acepta letras minúsculas.
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo 2: Demostración del método isspace:identifica espacios en blanco solamente - no tiene en cuenta ningún otro carácter (el resultado es entonces False).
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo 3: Demostración del método isupper():  es la versión en mayúscula de islower() - se concentra solo en letras mayúsculas.
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())


#El método join()
# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))


#El método lower() genera una copia de una cadena, reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas,
# y devuelve la cadena como resultado. Nuevamente, la cadena original permanece intacta.
# Demostración del método lower():
print("SiGmA=60".lower())


## Demostración del método the lstrip(): devuelve una cadena recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales.
# Demostración del método the lstrip():
print("[" + " tau ".lstrip() + "]")
#elimina inicios en la cadena
print("www.cisco.com".lstrip("w."))

#El método replace() con dos parámetros devuelve una copia de la cadena original en la que todas las apariciones del primer argumento
# han sido reemplazadas por el segundo argumento.
# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))



#El método rfind()
# Demostración del método rfind():
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))


#El método rstrip() Dos variantes del método rstrip() hacen casi lo mismo que el método lstrip, pero afecta el lado opuesto de la cadena.
# Demostración del método rstrip():
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))


#El método split() divide la cadena y crea una lista de todas las subcadenas detectadas. inversa del join
# Demostración del método split():
print("phi       chi\npsi".split())


#El método startswith() es un espejo del método endswith() - comprueba si una cadena dada comienza con la subcadena especificada.
# Demostración del método startswith():
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()


# Demostración del método strip():combina los efectos causados por rstrip() y lstrip() 
#- crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.
print("[" + "   aleph   ".strip() + "]")


#El método swapcase() crea una nueva cadena intercambiando todas las letras por
# mayúsculas o minúsculas dentro de la cadena original: los caracteres en mayúscula se convierten en minúsculas y viceversa.
# Demostración del método swapcase():
print("Yo sé que no sé nada.".swapcase())

print()

# Demostración del método title(): realiza una función algo similar cambia la primera letra de cada palabra a mayúsculas, convirtiendo todas las demás a minúsculas.
print("Yo sé que no sé nada. Part 1.".title())

print()

# Demostración del método upper(): hace una copia de la cadena de origen, reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas, y devuelve la cadena como resultado.
print("Yo sé que no sé nada. Part 2.".upper())


'Puntos Clave'
#Algunos de los métodos que ofrecen las cadenas son:

"""capitalize(): cambia todas las letras de la cadena a mayúsculas.
center(): centra la cadena dentro de una longitud conocida.
count(): cuenta las ocurrencias de un carácter dado.
join(): une todos los elementos de una tupla/lista en una cadena.
lower(): convierte todas las letras de la cadena en minúsculas.
lstrip(): elimina los caracteres en blanco al principio de la cadena.
replace(): reemplaza una subcadena dada con otra.
rfind(): encuentra una subcadena comenzando por el final de la cadena.
rstrip(): elimina los caracteres en blanco al final de la cadena.
split(): divide la cadena en una subcadena usando un delimitador dado.
strip(): elimina los espacios en blanco iniciales y finales.
swapcase(): intercambia las mayúsculas y minúsculas de las letras.
title(): hace que la primera letra de cada palabra sea mayúscula.
upper(): convierte todas las letras de la cadena en letras mayúsculas."""

#El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):

"""endswith(): ¿La cadena termina con una subcadena determinada?
isalnum(): ¿La cadena consta solo de letras y dígitos?
isalpha(): ¿La cadena consta solo de letras?
islower(): ¿La cadena consta solo de letras minúsculas?
isspace(): ¿La cadena consta solo de espacios en blanco?
isupper(): ¿La cadena consta solo de letras mayúsculas?
startswith(): ¿La cadena consta solo de letras mayúsculas?"""

