#funciones
def suma(x,y):
    return x+y
def resta(x,y):
    return x-y
def multiplicación(x,y):
    return x*y
def División(x,y):
    return x/y
n=int(0)
#ingreso de datos

while n!=5:
    x=int(input("ingrese el primer operando: "))
    y=int(input("ingrese el segundo operando: "))
    print("operaciones: \n1|suma\n2|resta\n3|multiplicación\n4|División\n5|reingresar numeros\n6|Salir\n")
    n=int(input("\nSeleccione su operación: "))
#procesamiento
    if n == 1:
        print("resultado = ",suma(x,y))
        n=5
    elif n == 2:
        print("resultado = ",resta(x,y))
        n=5
    elif n == 3:
        print("resultado = ",multiplicación(x,y))
        n=5
    elif n == 4:
        print("resultado = ",División(x,y))
        n=5
    elif n == 5:
        print("Regresando...")
        n=0
    elif n == 6:
        n=5
    else:
        print("**Numero incorecto repitalo: ")

print("Fin del programa")    