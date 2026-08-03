class Proveedor:

    def __init__(self, id_proveedor,nombre_proveedor,apellido_paterno,apellido_materno,telefono,email,direccion):
        self.id_proveedor = id_proveedor
        self.nombre_proveedor = nombre_proveedor
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def __str__(self):
     return (f"ID: {self.id_proveedor}, Nombre: {self.nombre_proveedor}, "
             f"Apellido Paterno: {self.apellido_paterno}, Apellido Materno: {self.apellido_materno}, "
             f"Teléfono: {self.telefono}, Email: {self.email}, Dirección: {self.direccion}")