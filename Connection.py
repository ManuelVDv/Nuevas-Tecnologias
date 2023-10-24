import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="conexion"
)

cursor = conn.cursor()

nombre = input("Nombre: ")
email = input("Email: ")

sql = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
val = (nombre, email)

cursor.execute(sql, val)

conn.commit()

cursor.close()
conn.close()

print("Dato registrado con éxito.")
