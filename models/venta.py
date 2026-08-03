class Venta:
    def __init__(self, id_venta, nombre_venta, usuario_id, ganancia, fecha, articulo):
        self.id_venta = id_venta
        self.nombre_venta = nombre_venta
        self.usuario_id = usuario_id
        self.ganancia = ganancia
        self.fecha = fecha
        self.articulo = articulo  # lista de id_producto

    def __str__(self):
        return (f"ID: {self.id_venta}, Nombre: {self.nombre_venta}, Usuario ID: {self.usuario_id}, "
                f"Ganancia: ${self.ganancia}, Fecha: {self.fecha}, Artículos: {self.articulo}")