db_usuarios = []

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo: ")
    contraseña = input("Ingrese su contraseña: ")

    usuario = {'nombre': nombre, 'correo': correo, 'contraseña': contraseña}
    db_usuarios.append(usuario)
    print("Registro completado.\n")

def iniciar_sesion():
    correo = input("Ingrese su correo: ")
    contraseña = input("Ingrese su contraseña: ")

    for usuario in db_usuarios:
        if usuario['correo'] == correo and usuario['contraseña'] == contraseña:
            print("Inicio de sesión exitoso.\n")
            return

    print(" Error\n ")

while True:
    print(" Menu: ")
    print(" 1. Registro ")
    print(" 2. Iniciar Sesión ")
    print(" 3. Salir ")

    opcion = input(" Elija una opción (1/2/3): ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
        print(" Saliendo... ")
        break
    else:
        print(" Error\n ")