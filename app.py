# import flet as ft 

from dao.producto_dao import ProductoDAO
from models.producto import Producto

def insertar_producto():
    producto_id = None
    producto_producto = input("\nEscriba el nombre del producto: ")
    producto_codigo = float(input("\nEscribe el precio del producto:"))
    producto_precio = int(input("\nEscribe la cantidad del producto:"))

    print("\n-----------Proveedores-----------")
    print("1. Don Pepe")
    print("2. Don Juan")
    print("3. Don Paco")

    producto_proveedor = int(input("\nEscriba el ID del proveedor: "))

    producto_descripcion = input("\nEscriba la descripción del producto: ")

    print("\n-----------Categorias-----------")
    print("1. Libreta")
    print("2. Cuaderno")
    print("3. Bolso")
    print("4. Lápiz")
    print("5. Borrador")

    producto_categoria = int(input("\nEscriba el ID de la categoría: "))

    print("\n-----------Marcas-----------")
    print("1. Vincy")
    print("2. Mapita")
    print("3. Faber-Castell")

    producto_marca = int(input("\nEscriba el ID de la marca: "))

    try:
        producto = Producto(
            id_producto=producto_id,
            nombre=producto_producto,
            precio=producto_codigo,
            cantidad=producto_precio,
            id_proveedor=producto_proveedor,
            descripcion=producto_descripcion,
            id_categoria=producto_categoria,
            id_marca=producto_marca
        )

        producto_dao = ProductoDAO()
        producto_dao.insertar(producto)
        print("Producto insertado correctamente.")

    except Exception as e:
        print(f"Error al insertar el producto")
        print(e)


def ver_productos():
    try:
        producto_dao = ProductoDAO()
        productos = producto_dao.obtener_todos()

        if productos:
            for producto in productos:
                print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}, ID Proveedor: {producto.id_proveedor}, Descripción: {producto.descripcion}, ID Categoría: {producto.id_categoria}, ID Marca: {producto.id_marca}")

        else:
            print("No se encontraron productos.")

    except Exception as e:
        print(f"Error al obtener los productos")
        print(e)

def main():
    while True:
        print("\n--- Menú de Productos ---")
        print("1. Insertar producto")
        print("2. Ver productos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            insertar_producto()
        elif opcion == "2":
            ver_productos()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()