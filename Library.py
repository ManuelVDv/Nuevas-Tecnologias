
dbLibrary = [] # Lista para almacenear datos.
def agregar_libro(): # Función para agregar un elemento a la lista.
    book = input(" Ingresar libro: ")  # input para registrar un nuevo elemento.
    dbLibrary.append(book)  # Agregar un nuevo elemento a la lista existente.
def actualizar_libro(): # Función para actualizar un elemento de la lista.
    book = input(" Renovar libro: ")  # input para solicitar el elemento que se va actualizar.
    if book in dbLibrary:  # Verificar si el libro exite.
        new_book = input(" Ingresar nuevo nombre: ")  # input para actualizar el elemento elegido.
        index = dbLibrary.index(book)  # Obtener la posicion de un elemento de la lista.
        dbLibrary[index] = new_book  # Actualizar el nombre del libro.
        print(" OK ")  # Indicar si fue un exito.
    else:
        print(" Error ")  # Si el libro no está en la lista, mostramos un mensaje de error.
def eliminar_libro(): # Función para eliminar un libro de la lista.
    book = input(" Eliminar Libro: ")  # Solicitamos al usuario el nombre del libro a eliminar.
    if book in dbLibrary:  # Verificamos si el libro está en la lista.
        dbLibrary.remove(book)  # Eliminamos el libro de la lista.
        print(" OK ")  # Informamos que la operación fue exitosa.
    else:
        print(" Error ")  # Si el libro no está en la lista, mostramos un mensaje de error.
def lista_libros(): # Función para listar los libros en la lista.
    if len(dbLibrary) == 0:  # Verificamos si la lista está vacía.
        print(" Librería vacía ")  # Si la lista está vacía, mostramos un mensaje.
    else:
        print(" Libros Actuales: ")  # Si la lista no está vacía, mostramos los libros.
        for book in dbLibrary:
            print(book)  # Mostramos cada libro en la lista.


while True: # Bucle principal que muestra las opciones al usuario y realiza las acciones correspondientes.
    print(" \nOpciones: ")
    print(" A- Agregar ")
    print(" B- Actualizar ")
    print(" C- Eliminar ")
    print(" D- Listar ")
    print(" E- Salida ")

    choice = input("Elija 1, 2, 3, 4, 5: ") # input para seleccionar la opciones del while.
    if choice == "A":
        agregar_libro() # Funcion agregar.
    elif choice == "B":
        actualizar_libro() # Funcion actualizar.
    elif choice == "C":
        eliminar_libro() # Funcion eliminar.
    elif choice == "D":
        lista_libros() # Funcion listar.
    elif choice == "E":
        break # Terminar
    else:
        print(" Error ") # Error por si el usuario elige una opcion que no existe.