# import mysql.connector

# def conectar():
#     return mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "root",
#         database = "tienda_conectada"
#     )

# def insertar_cliente(nombre, email, telefono):
#     db = conectar()
#     cursor = db.cursor()
#     sql = "INSERT INTO cliente (nombre, email, telefono) VALUES (%s, %s, %s)"
#     cursor.execute(sql, (nombre, email, telefono))
#     db.commit()
#     db.close()

# def listar_clientes():
#     db = conectar()
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM cliente")
#     resultados = cursor.fetchall()
#     db.close()
#     return resultados

# def buscar_por_id(id_cliente):
#     db = conectar()
#     cursor = db.cursor()
#     cursor.execute("SELECT * FROM cliente WHERE id = %s", (id_cliente,))
#     resultado = cursor.fetchone()
#     db.close()
#     return resultado

# ## MENU ##
# while True:
#     print("---- Menú ----")
#     print("1. Agregar clientes")
#     print("2. Listar clientes")
#     print("3. Buscar cliente por ID")
#     print("4. Salir")

#     opcion = input("Seleccione una opcion:")

#     if opcion == "1":
#         nombre = input("Nombre: ")
#         email = input("Email: ")
#         telefono = input("Telefono: ")
#         insertar_cliente(nombre,email,telefono)
#         print("Cliente agregado exitosamente!")

#     elif opcion == "2":
#         clientes= listar_clientes()
#         for c in clientes:
#             print(c)
        
#     elif opcion == "3":
#         id_buscado = int(input("Ingrese ID: "))
#         cliente = buscar_por_id(id_buscado)
#         print(cliente if cliente else "No encontrado")

#     elif opcion == "4":
#         print("Saliendo...")
#         break

#     else:
#         print("Opcion incorrecta!")
        
        
## Práctica transacciones ##

# def conectar():
#     return mysql.connector.connect(
#         host = "localhost",
#         user = "root",
#         password = "root",
#         database = "banco"
#     )

# def transferir(id_origen, id_destino, monto):
#     db = conectar()
#     cursor = db.cursor()
    
#     try:
#         # Iniciar transaccion
#         db.start_transaction()

#         # Verificar el saldo
#         cursor.execute("SELECT saldo FROM cuenta WHERE id = %s FOR UPDATE", (id_origen,))
#         saldo_origen = cursor.fetchone()[0]

#         if saldo_origen < monto:
#             raise Exception("Saldo insuficiente!!")
        
#         # Descontar monto al origen
#         cursor.execute("UPDATE cuenta SET saldo = saldo - %s WHERE id = %s", (monto, id_origen))

#         # Acreditar al destino
#         cursor.execute("UPDATE cuenta SET saldo = saldo + %s WHERE id = %s", (monto, id_destino))

#         # Confirmo los cambios 
#         db.commit()
#         print("Transferencia realizada con éxito!!!")
#     except Exception as e:
#         db.rollback()
#         print("Error:", e)
#         print("Transaccion revertida")
        
#     finally:
#         db.close()
        
        
# def mostrar_saldos():
#     db = conectar()
#     cursor = db.cursor()
#     cursor.execute("SELECT id, titular, saldo FROM cuenta")
#     cuentas = cursor.fetchall()
#     db.close()

#     print("---- Saldos actuales ----")
#     for c in cuentas:
#         print(f"ID {c[0]} | {c[1]} | Saldo: ${c[2]:.2f}")
#     print("------------------------------")
    
# print("Saldos antes:")
# mostrar_saldos()

# transferir(1,2,250)

# print("Saldos despues:")
# mostrar_saldos()

# transferir(1,2,1000)

import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password="root",
    database= "test_db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS PERSONA (
    ID INT PRIMARY KEY,
               NOMBRE VARCHAR(50) NOT NULL,
               EDAD INT NOT NULL,
               DIRECCION VARCHAR(100)           
               );
""")

print("Tabla creada exitosamente!!")

conn.commit()
# conn.close()

conn.cursor()
cursor.execute(
    "INSERT INTO PERSONA (ID,NOMBRE,EDAD,DIRECCION) VALUES (%s, %s,%s,%s)", (1, "Pablo", 32, "Av. Chaco 123")
)

conn.commit()
print("Registros guardados exitosamente!")

cursor.execute("SELECT ID, NOMBRE, EDAD, DIRECCION FROM PERSONA")

for row in cursor:
    print("ID = ", row[0])
    print("NOMBRE = ", row[1])
    print("EDAD = ", row[2])
    print("DIRECCION = ", row[3])
    
print("Consulta exitosa!")

cursor.execute("UPDATE PERSONA SET DIRECCION = %s WHERE ID = %s", ("Av. Alvear 300", 1))
conn.commit()

cursor.execute("SELECT ID, NOMBRE, DIRECCION FROM PERSONA")

for row in cursor:
    print("ID = ", row[0])
    print("NOMBRE = ", row[1])
    print("DIRECCION = ", row[2])

print("Fila actualizada!")

cursor.execute("DELETE FROM PERSONA WHERE ID = %s", (1,))
conn.commit()

print("Filas eliminadas:", cursor.rowcount)

cursor.execute("SELECT ID, NOMBRE, EDAD, DIRECCION FROM PERSONA")

for row in cursor:
    print("ID = ", row[0])
    print("NOMBRE = ", row[1])
    print("EDAD = ", row[2])
    print("DIRECCION = ", row[3])

