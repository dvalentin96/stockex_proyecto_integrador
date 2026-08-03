from database.conexion import Conexion
from models.venta import Venta

class VentaDAO:

    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute("SELECT * FROM ventas")
        registros = cursor.fetchall()

        ventas = []
        for registro in registros:
            venta = Venta(
                id_venta=registro[0],
                nombre_venta=registro[1],
                usuario_id=registro[2],
                ganancia=registro[3],
                fecha=registro[4],
                articulo=registro[5]
            )
            ventas.append(venta)

        cursor.close()
        conexion.close()
        return ventas

    def obtener_por_id(self, id_venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute("SELECT * FROM ventas WHERE id_venta = %s", (id_venta,))
        registro = cursor.fetchone()

        venta = None
        if registro:
            venta = Venta(
                id_venta=registro[0],
                nombre_venta=registro[1],
                usuario_id=registro[2],
                ganancia=registro[3],
                fecha=registro[4],
                articulo=registro[5]
            )

        cursor.close()
        conexion.close()
        return venta

    def insertar(self, venta):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute(
            "INSERT INTO ventas (nombre_venta, usuario_id, ganancia, fecha, articulo) VALUES (%s, %s, %s, %s, %s)",
            (venta.nombre_venta, venta.usuario_id, venta.ganancia, venta.fecha, venta.articulo)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def obtener_por_rango_fechas(self, fecha_inicio, fecha_fin):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute(
            "SELECT * FROM ventas WHERE fecha BETWEEN %s AND %s ORDER BY fecha",
            (fecha_inicio, fecha_fin)
        )
        registros = cursor.fetchall()

        ventas = []
        for registro in registros:
            venta = Venta(
                id_venta=registro[0],
                nombre_venta=registro[1],
                usuario_id=registro[2],
                ganancia=registro[3],
                fecha=registro[4],
                articulo=registro[5]
            )
            ventas.append(venta)

        cursor.close()
        conexion.close()
        return ventas