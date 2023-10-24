db_usuarios = []
db_bicicletas = {
    'b01': {'origen': 'Suramericana', 'destino': 'San Antonio', 'disponible': True},
    'b02': {'origen': 'Manrique', 'destino': 'Milagrosa', 'disponible': True},
    'b03': {'origen': 'Estadio', 'destino': 'Suramericana', 'disponible': False},
    'b04': {'origen': 'Robledo', 'destino': 'los colores', 'disponible': True},
}


def usuario_existente(numero_tarjeta):
    for usuario in db_usuarios:
        if 'tarjeta' in usuario and usuario['tarjeta'] == numero_tarjeta:
            return True
    return False


def register():
    name = input("Ingrese su Nombre: ")
    email = input("Ingrese un correo: ")
    phone = input("Ingrese Num Telefono: ")
    password = input("Ingrese contraseña: ")
    tarjeta = input("Ingrese su número de tarjeta: ")

    usuario = {'name': name, 'email': email, 'phone': phone, 'password': password, 'tarjeta': tarjeta}
    db_usuarios.append(usuario)
    print("***Registro completo****\n")


def login():
    email = input("Ingrese su correo: ")
    phone = input("Ingrese su telefono: ")

    for usuario in db_usuarios:
        if usuario.get('email') == email and usuario.get('phone') == phone:
            print("***Inicio de sesión completo***\n")
            return
    print("Información incorrecta, intente otra vez.\n")


def prestar_bicicleta():
    numero_tarjeta = input("Ingrese su número de tarjeta: ")
    if usuario_existente(numero_tarjeta):
        for bicicleta, info in db_bicicletas.items():
            if info['disponible']:
                print(f"Bicicleta: {bicicleta}, Origen: {info['origen']}, Destino: {info['destino']}")

        bicicleta_seleccionada = input("Seleccione una bicicleta para prestar: ")

        if bicicleta_seleccionada in db_bicicletas and db_bicicletas[bicicleta_seleccionada]['disponible']:
            db_bicicletas[bicicleta_seleccionada]['disponible'] = False
            print(f"Has prestado la bicicleta {bicicleta_seleccionada}\n")
        else:
            print("Bicicleta no válida o ya prestada.\n")
    else:
        print("Usuario no encontrado. Por favor, regístrese primero.\n")


def consultar_usuario():
    numero_tarjeta = input("Ingrese su número de tarjeta: ")
    if usuario_existente(numero_tarjeta):
        for usuario in db_usuarios:
            if 'tarjeta' in usuario and usuario['tarjeta'] == numero_tarjeta:
                print(f"Nombre: {usuario['name']}")
                print(f"Email: {usuario['email']}")
                print(f"Teléfono: {usuario['phone']}")
                print(f"Número de Tarjeta: {usuario['tarjeta']}\n")
                return
    else:
        print("Usuario no encontrado. Por favor, regístrese primero.\n")


while True:
    print(" Menu: ")
    print(" 1. Registro ")
    print(" 2. Iniciar Sesion ")
    print(" 3. Prestar Bicicleta ")
    print(" 4. Consultar Usuario ")
    print(" 5. Salir ")

    choice = input(" Opcion: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        prestar_bicicleta()
    elif choice == '4':
        consultar_usuario()
    elif choice == '5':
        print(" Saliendo... ")
        break
    else:
        print("Error\n")