
# Definicion de una funcion
def  main():
    print("OK")
# Llamado de la funcion
main()

# Funcion con parametros
def mainP(name):
    print(f"OK {name}")
# Llamado
mainP("Manuel")

# Imprimir lista
def printList(*args):
    print(f"OK {args}")

# Llamado
printList("OK", "Manuel", "Jhon", "Suzan")

# Funciones con retorno
def add(num1, num2):
    return num1 + num2
# Operacion
resultAdd = add(5, 9)
# Llamado
print(resultAdd)

#
user = ["1", "Manuel", "Valencia"]

def List(list):
    for i in range(len(list)):
        print(user[i])
# Llamado
List(user)