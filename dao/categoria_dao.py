from database.conexion import Conexion
from models.categoria import Categoria

class CategoriaDAO:

    def obtener_todos(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute("SELECT * FROM categorias")
        registros = cursor.fetchall()

        categorias = []
        for registro in registros:
            categoria = Categoria(
                id_categoria=registro[0],
                nombre_categoria=registro[1],
                descripcion=registro[2]
            )
            categorias.append(categoria)

        cursor.close()
        conexion.close()
        return categorias

    def obtener_por_id(self, id_categoria):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute("SELECT * FROM categorias WHERE id_categoria = %s", (id_categoria,))
        registro = cursor.fetchone()

        categoria = None
        if registro:
            categoria = Categoria(
                id_categoria=registro[0],
                nombre_categoria=registro[1],
                descripcion=registro[2]
            )

        cursor.close()
        conexion.close()
        return categoria

    def insertar(self, categoria):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute(
            "INSERT INTO categorias (nombre_categoria, descripcion) VALUES (%s, %s)",
            (categoria.nombre_categoria, categoria.descripcion)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def actualizar(self, categoria):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute(
            "UPDATE categorias SET nombre_categoria = %s, descripcion = %s WHERE id_categoria = %s",
            (categoria.nombre_categoria, categoria.descripcion, categoria.id_categoria)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self, id_categoria):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        conexion.rollback()

        cursor.execute("DELETE FROM categorias WHERE id_categoria = %s", (id_categoria,))
        conexion.commit()
        cursor.close()
        conexion.close()