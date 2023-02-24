def edad ():
    
    a=int(input("ingrese su edad"))
    
    assert a>17," usted no a nacido menor de edad, por favor que el sistema lo use un cucho"
    print("tas viejo weon")
    edad()
edad()
