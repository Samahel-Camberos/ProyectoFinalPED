import csv
import mysql.connector


def insertardatos(producto_id, calificacion_id, precio_id,ID_PaginaWeb):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="administrador",
        database="nike"
    )

    # Crear un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Abrir el archivo CSV y leer los datos
    with open("dataset/amazon_12.csv", 'r') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        next(lector_csv)  # Ignorar la primera fila (encabezados)

        # Insertar cada fila en la base de datos
        for fila in lector_csv:
            # Insertar en la tabla de Productos
            cursor.execute("INSERT INTO Productos (nombre, género) VALUES (%s, %s)", (fila[0], fila[1]))
            producto_id = cursor.lastrowid

            # Insertar en la tabla de Calificaciones
            cursor.execute("INSERT INTO Calificaciones (calificación, opiniones) VALUES (%s, %s)", (fila[2], fila[3]))
            calificacion_id = cursor.lastrowid

            cursor.execute("INSERT INTO PaginasWeb (nombre) VALUES (%s)", (fila[5],))
            calificacion_id1 = cursor.lastrowid

            # Insertar en la tabla de Precios
            precio = fila[4] if fila[4] else None
            cursor.execute("INSERT INTO Precios (precio) VALUES (%s)", (precio,))
            precio_id = cursor.lastrowid

            # Insertar en la tabla de Opiniones
            cursor.execute("INSERT INTO Opiniones (ID_Producto, ID_Calificación, ID_Precio, ID_PaginaWeb) VALUES (%s, %s, %s,%s)",
                           (producto_id, calificacion_id, precio_id,calificacion_id1))

    # Confirmar los cambios
    conexion.commit()


if __name__ == "__main__":
    insertardatos(1,1,