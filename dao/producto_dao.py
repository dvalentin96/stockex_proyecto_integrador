from database.conexion import Conexion
from models.producto import Producto

class ProductoDAO:

    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        registros = cursor.fetchall()

        productos = []
        for registro in registros:
            producto = Producto(
                id_producto=registro[0],
                nombre=registro[1],
                precio=registro[2],
                cantidad=registro[3],
                id_proveedor=registro[4],
                descripcion=registro[5],
                id_categoria=registro[6],
                id_marca=registro[7]
            )
            productos.append(producto)

        cursor.close()
        conexion.close()
        return productos
        
    def insertar (self, producto):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio, cantidad, id_proveedor, descripcion, id_categoria, id_marca) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (producto.nombre, producto.precio, producto.cantidad, producto.id_proveedor, producto.descripcion, producto.id_categoria, producto.id_marca)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar (self, producto):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "UPDATE productos SET nombre = %s, precio = %s, cantidad = %s, id_proveedor = %s, descripcion = %s, id_categoria = %s, id_marca = %s WHERE id_producto = %s",
            (producto.nombre, producto.precio, producto.cantidad, producto.id_proveedor, producto.descripcion, producto.id_categoria, producto.id_marca, producto.id_producto)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, id_producto):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
        conexion.commit()
        cursor.close()
        conexion.close()
