class Categoria:
    def __init__(self, id_categoria, nombre_categoria, descripcion):
        self.id_categoria = id_categoria
        self.nombre_categoria = nombre_categoria
        self.descripcion = descripcion

    def __str__(self):
        return (f"ID: {self.id_categoria}, Nombre: {self.nombre_categoria}, "
                f"Descripción: {self.descripcion}")