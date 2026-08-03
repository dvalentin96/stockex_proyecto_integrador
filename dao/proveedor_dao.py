from database.conexion import Conexion
from models.proveedor import Proveedor

class ProveedorDAO:

    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute("SELECT * FROM proveedores")
        registros = cursor.fetchall()

        proveedores = []
        for registro in registros:
            proveedor = Proveedor(
                id_proveedor=registro[0],
                nombre_proveedor=registro[1],
                apellido_paterno=registro[2],
                apellido_materno=registro[3],
                telefono=registro[4],
                email=registro[5],
                direccion=registro[6]
            )
            proveedores.append(proveedor)

        cursor.close()
        conexion.close()
        return proveedores

    def obtener_por_id(self, id_proveedor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute("SELECT * FROM proveedores WHERE id_proveedor = %s", (id_proveedor,))
        registro = cursor.fetchone()

        proveedor = None
        if registro:
            proveedor = Proveedor(
                id_proveedor=registro[0],
                nombre_proveedor=registro[1],
                apellido_paterno=registro[2],
                apellido_materno=registro[3],
                telefono=registro[4],
                email=registro[5],
                direccion=registro[6]
            )

        cursor.close()
        conexion.close()
        return proveedor

    def insertar(self, proveedor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute(
            "INSERT INTO proveedores (nombre_proveedor, apellido_paterno, apellido_materno, telefono, email, direccion) VALUES (%s, %s, %s, %s, %s, %s)",
            (proveedor.nombre_proveedor, proveedor.apellido_paterno, proveedor.apellido_materno, proveedor.telefono, proveedor.email, proveedor.direccion)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, proveedor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute(
            "UPDATE proveedores SET nombre_proveedor = %s, apellido_paterno = %s, apellido_materno = %s, telefono = %s, email = %s, direccion = %s WHERE id_proveedor = %s",
            (proveedor.nombre_proveedor, proveedor.apellido_paterno, proveedor.apellido_materno, proveedor.telefono, proveedor.email, proveedor.direccion, proveedor.id_proveedor)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, id_proveedor):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute("DELETE FROM proveedores WHERE id_proveedor = %s", (id_proveedor,))
        conexion.commit()
        cursor.close()
        conexion.close()
