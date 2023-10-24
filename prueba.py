import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Establecer conexión con la base de datos MySQL
def conectar():
    global conn, cursor
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="mi_bd")
    cursor = conn.cursor()

# Función para iniciar sesión
def login():
    conectar()
    usuario = entry_usuario.get()
    password = entry_password.get()

    query = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
    cursor.execute(query, (usuario, password))
    result = cursor.fetchone()

    if result:
        show_menu()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear menu principal
def show_menu():
    root.withdraw()
    menu = Toplevel()
    menu.title("Menú Principal")

    # Crear elementos del menu
    tabla = ttk.Treeview(menu, columns=("id", "nombre", "edad"), show="headings")
    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("edad", text="Edad")
    tabla.pack()

    # Cargar registros desde la base de datos
    def cargar_registros():
        tabla.delete(*tabla.get_children())
        cursor.execute("SELECT * FROM registros ORDER BY id DESC")
        registros = cursor.fetchall()
        for registro in registros:
            tabla.insert("", 0, values=registro)

    cargar_registros()

    # Funciones de callback
    def on_validate(P):
        return True

    def on_invalid(P):
        return True

    # Lambda para manejar el evento de cierre del menu
    menu.protocol("WM_DELETE_WINDOW", lambda: root.deiconify())

    root.deiconify()

# Iniciar aplicación
root = Tk()
root.title("Iniciar sesión")

label_usuario = Label(root, text="Usuario:")
label_usuario.pack()

entry_usuario = Entry(root)
entry_usuario.pack()

label_password = Label(root, text="Contraseña:")
label_password.pack()

entry_password = Entry(root, show="*")
entry_password.pack()

button_login = Button(root, text="Iniciar sesión", command=login)
button_login.pack()

root.mainloop()