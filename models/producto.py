class Producto:
    def __init__(self, id_producto, nombre, precio, cantidad, id_proveedor, descripcion, id_categoria, id_marca):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.id_proveedor = id_proveedor
        self.descripcion = descripcion
        self.id_categoria = id_categoria
        self.id_marca = id_marca

    def __str__(self):
        return (f"Producto(id = {self.id_producto}, nombre = {self.nombre}, precio = {self.precio}, cantidad = {self.cantidad}, "
                f"proveedor = {self.id_proveedor}, descripcion = {self.descripcion}, categoria = {self.id_categoria}, marca = {self.id_marca})")
    
        