# import flet as ft 

from dao.producto_dao import ProductoDAO
from models.producto import Producto

from dao.proveedor_dao import ProveedorDAO
from models.proveedor import Proveedor

from dao.categoria_dao import CategoriaDAO
from models.categoria import Categoria

from dao.venta_dao import VentaDAO
from models.venta import Venta

from services.reporte_ventas import generar_reporte_ventas_pdf

from datetime import date

def insertar_producto():
    producto_id = None
    producto_nombre = input("\nEscriba el nombre del producto: ")
    producto_precio = float(input("\nEscribe el precio del producto: "))
    producto_cantidad = int(input("\nEscribe la cantidad del producto: "))

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
            nombre=producto_nombre,
            precio=producto_precio,
            cantidad=producto_cantidad,
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
                print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Precio: {producto.precio}, "
                      f"Cantidad: {producto.cantidad}, ID Proveedor: {producto.id_proveedor}, "
                      f"Descripción: {producto.descripcion}, ID Categoría: {producto.id_categoria}, "
                      f"ID Marca: {producto.id_marca}")
        else:
            print("No se encontraron productos.")

    except Exception as e:
        print(f"Error al obtener los productos")
        print(e)


def ver_producto_por_id():
    try:
        producto_id = int(input("\nEscriba el ID del producto a buscar: "))

        producto_dao = ProductoDAO()
        producto = producto_dao.obtener_por_id(producto_id)

        if producto:
            print(f"ID: {producto.id_producto}, Nombre: {producto.nombre}, Precio: {producto.precio}, "
                  f"Cantidad: {producto.cantidad}, ID Proveedor: {producto.id_proveedor}, "
                  f"Descripción: {producto.descripcion}, ID Categoría: {producto.id_categoria}, "
                  f"ID Marca: {producto.id_marca}")
        else:
            print("No se encontró ningún producto con ese ID.")

    except Exception as e:
        print(f"Error al buscar el producto")
        print(e)


def actualizar_producto():
    try:
        producto_id = int(input("\nEscriba el ID del producto a actualizar: "))

        producto_dao = ProductoDAO()
        producto_existente = producto_dao.obtener_por_id(producto_id)

        if not producto_existente:
            print("No se encontró ningún producto con ese ID.")
            return

        print(f"\nProducto actual -> Nombre: {producto_existente.nombre}, Precio: {producto_existente.precio}, "
              f"Cantidad: {producto_existente.cantidad}, Descripción: {producto_existente.descripcion}")

        producto_nombre = input("\nEscriba el nuevo nombre del producto: ")
        producto_precio = float(input("Escriba el nuevo precio del producto: "))
        producto_cantidad = int(input("Escriba la nueva cantidad del producto: "))

        print("\n-----------Proveedores-----------")
        print("1. Don Pepe")
        print("2. Don Juan")
        print("3. Don Paco")
        producto_proveedor = int(input("Escriba el nuevo ID del proveedor: "))

        producto_descripcion = input("Escriba la nueva descripción del producto: ")

        print("\n-----------Categorias-----------")
        print("1. Libreta")
        print("2. Cuaderno")
        print("3. Bolso")
        print("4. Lápiz")
        print("5. Borrador")
        producto_categoria = int(input("Escriba el nuevo ID de la categoría: "))

        print("\n-----------Marcas-----------")
        print("1. Vincy")
        print("2. Mapita")
        print("3. Faber-Castell")
        producto_marca = int(input("Escriba el nuevo ID de la marca: "))

        producto_actualizado = Producto(
            id_producto=producto_id,
            nombre=producto_nombre,
            precio=producto_precio,
            cantidad=producto_cantidad,
            id_proveedor=producto_proveedor,
            descripcion=producto_descripcion,
            id_categoria=producto_categoria,
            id_marca=producto_marca
        )

        producto_dao.actualizar(producto_actualizado)
        print("Producto actualizado correctamente.")

    except Exception as e:
        print(f"Error al actualizar el producto")
        print(e)


def eliminar_producto():
    try:
        producto_id = int(input("\nEscriba el ID del producto a eliminar: "))

        producto_dao = ProductoDAO()
        producto_existente = producto_dao.obtener_por_id(producto_id)

        if not producto_existente:
            print("No se encontró ningún producto con ese ID.")
            return

        confirmacion = input(f"¿Seguro que desea eliminar '{producto_existente.nombre}'? (s/n): ")
        if confirmacion.lower() == "s":
            producto_dao.eliminar(producto_id)
            print("Producto eliminado correctamente.")
        else:
            print("Operación cancelada.")

    except Exception as e:
        print(f"Error al eliminar el producto")
        print(e)

# PROVEEDOR
def insertar_proveedor():
    proveedor_id = None
    proveedor_nombre = input("\nEscriba el nombre del proveedor: ")
    proveedor_apellido_paterno = input("Escriba el apellido paterno del proveedor: ")
    proveedor_apellido_materno = input("Escriba el apellido materno del proveedor: ")
    proveedor_telefono = input("Escriba el teléfono del proveedor: ")
    proveedor_email = input("Escriba el email del proveedor: ")
    proveedor_direccion = input("Escriba la dirección del proveedor: ")

    try:
        proveedor = Proveedor(
            id_proveedor=proveedor_id,
            nombre_proveedor=proveedor_nombre,
            apellido_paterno=proveedor_apellido_paterno,
            apellido_materno=proveedor_apellido_materno,
            telefono=proveedor_telefono,
            email=proveedor_email,
            direccion=proveedor_direccion
        )

        proveedor_dao = ProveedorDAO()
        proveedor_dao.insertar(proveedor)
        print("Proveedor insertado correctamente.")

    except Exception as e:
        print(f"Error al insertar el proveedor")
        print(e)
    
def ver_proveedores():
    try:
        proveedor_dao = ProveedorDAO()
        proveedores = proveedor_dao.obtener_todos()

        if proveedores:
            for proveedor in proveedores:
                print(proveedor)
        else:
            print("No se encontraron proveedores.")

    except Exception as e:
        print(f"Error al obtener los proveedores")
        print(e)


def ver_proveedor_por_id():
    try:
        proveedor_id = int(input("\nEscriba el ID del proveedor a buscar: "))

        proveedor_dao = ProveedorDAO()
        proveedor = proveedor_dao.obtener_por_id(proveedor_id)

        if proveedor:
            print(proveedor)
        else:
            print("No se encontró ningún proveedor con ese ID.")

    except Exception as e:
        print(f"Error al buscar el proveedor")
        print(e)


def actualizar_proveedor():
    try:
        proveedor_id = int(input("\nEscriba el ID del proveedor a actualizar: "))

        proveedor_dao = ProveedorDAO()
        proveedor_existente = proveedor_dao.obtener_por_id(proveedor_id)

        if not proveedor_existente:
            print("No se encontró ningún proveedor con ese ID.")
            return

        print(f"\nProveedor actual -> {proveedor_existente}")

        proveedor_nombre = input("\nEscriba el nuevo nombre del proveedor: ")
        proveedor_apellido_paterno = input("Escriba el nuevo apellido paterno del proveedor: ")
        proveedor_apellido_materno = input("Escriba el nuevo apellido materno del proveedor: ")
        proveedor_telefono = input("Escriba el nuevo teléfono del proveedor: ")
        proveedor_email = input("Escriba el nuevo email del proveedor: ")
        proveedor_direccion = input("Escriba la nueva dirección del proveedor: ")

        proveedor_actualizado = Proveedor(
            id_proveedor=proveedor_id,
            nombre_proveedor=proveedor_nombre,
            apellido_paterno=proveedor_apellido_paterno,
            apellido_materno=proveedor_apellido_materno,
            telefono=proveedor_telefono,
            email=proveedor_email,
            direccion=proveedor_direccion
        )

        proveedor_dao.actualizar(proveedor_actualizado)
        print("Proveedor actualizado correctamente.")

    except Exception as e:
        print(f"Error al actualizar el proveedor")
        print(e)


def eliminar_proveedor():
    try:
        proveedor_id = int(input("\nEscriba el ID del proveedor a eliminar: "))

        proveedor_dao = ProveedorDAO()
        proveedor_existente = proveedor_dao.obtener_por_id(proveedor_id)

        if not proveedor_existente:
            print("No se encontró ningún proveedor con ese ID.")
            return

        confirmacion = input(f"¿Seguro que desea eliminar a '{proveedor_existente.nombre_proveedor}'? (s/n): ")
        if confirmacion.lower() == "s":
            proveedor_dao.eliminar(proveedor_id)
            print("Proveedor eliminado correctamente.")
        else:
            print("Operación cancelada.")

    except Exception as e:
        print(f"Error al eliminar el proveedor")
        print(e)

def insertar_categoria():
    categoria_id = None
    categoria_nombre = input("\nEscriba el nombre de la categoría: ")
    categoria_descripcion = input("Escriba la descripción de la categoría: ")

    try:
        categoria = Categoria(
            id_categoria=categoria_id,
            nombre_categoria=categoria_nombre,
            descripcion=categoria_descripcion
        )

        categoria_dao = CategoriaDAO()
        categoria_dao.insertar(categoria)
        print("Categoría insertada correctamente.")

    except Exception as e:
        print(f"Error al insertar la categoría")
        print(e)


def ver_categorias():
    try:
        categoria_dao = CategoriaDAO()
        categorias = categoria_dao.obtener_todos()

        if categorias:
            for categoria in categorias:
                print(categoria)
        else:
            print("No se encontraron categorías.")

    except Exception as e:
        print(f"Error al obtener las categorías")
        print(e)


def ver_categoria_por_id():
    try:
        categoria_id = int(input("\nEscriba el ID de la categoría a buscar: "))

        categoria_dao = CategoriaDAO()
        categoria = categoria_dao.obtener_por_id(categoria_id)

        if categoria:
            print(categoria)
        else:
            print("No se encontró ninguna categoría con ese ID.")

    except Exception as e:
        print(f"Error al buscar la categoría")
        print(e)


def actualizar_categoria():
    try:
        categoria_id = int(input("\nEscriba el ID de la categoría a actualizar: "))

        categoria_dao = CategoriaDAO()
        categoria_existente = categoria_dao.obtener_por_id(categoria_id)

        if not categoria_existente:
            print("No se encontró ninguna categoría con ese ID.")
            return

        print(f"\nCategoría actual -> {categoria_existente}")

        categoria_nombre = input("\nEscriba el nuevo nombre de la categoría:")
        categoria_descripcion = input("Escriba la nueva descripción de la categoría: ")

        categoria_actualizada = Categoria(
            id_categoria=categoria_id,
            nombre_categoria=categoria_nombre,
            descripcion=categoria_descripcion
        )

        categoria_dao.actualizar(categoria_actualizada)
        print("Categoría actualizada correctamente.")

    except Exception as e:
        print(f"Error al actualizar la categoría")
        print(e)


def eliminar_categoria():
    try:
        categoria_id = int(input("\nEscriba el ID de la categoría a eliminar: "))

        categoria_dao = CategoriaDAO()
        categoria_existente = categoria_dao.obtener_por_id(categoria_id)

        if not categoria_existente:
            print("No se encontró ninguna categoría con ese ID.")
            return

        confirmacion = input(f"¿Seguro que desea eliminar '{categoria_existente.nombre_categoria}'? (s/n): ")
        if confirmacion.lower() == "s":
            categoria_dao.eliminar(categoria_id)
            print("Categoría eliminada correctamente.")
        else:
            print("Operación cancelada.")

    except Exception as e:
        print(f"Error al eliminar la categoría")
        print(e)

def registrar_venta():
    producto_dao = ProductoDAO()
    venta_dao = VentaDAO()

    productos_vendidos = []  
    detalle_ticket = []       
    ganancia_total = 0.0
    seguir_agregando = True

    print("\n----------- Registrar Venta -----------")

    while seguir_agregando:
        productos = producto_dao.obtener_todos()
        if not productos:
            print("No hay productos disponibles.")
            return

        print("\nProductos disponibles:")
        for producto in productos:
            print(f"ID: {producto.id_producto} | {producto.nombre} | Precio: ${producto.precio} | Stock: {producto.cantidad}")

        try:
            id_producto = int(input("\nEscriba el ID del producto a vender: "))
            producto = producto_dao.obtener_por_id(id_producto)

            if not producto:
                print("No se encontró ningún producto con ese ID.")
                continue

            cantidad_vender = int(input(f"¿Cuántas unidades de '{producto.nombre}' desea vender? "))

            if cantidad_vender <= 0:
                print("La cantidad debe ser mayor a 0.")
                continue

            if cantidad_vender > producto.cantidad:
                print(f"Stock insuficiente. Solo hay {producto.cantidad} unidades disponibles.")
                continue

            subtotal = float(producto.precio) * cantidad_vender
            ganancia_total += subtotal

            producto.cantidad -= cantidad_vender
            producto_dao.actualizar(producto)

            productos_vendidos.append(producto.id_producto)
            detalle_ticket.append({
                "nombre": producto.nombre,
                "cantidad": cantidad_vender,
                "precio_unitario": float(producto.precio),
                "subtotal": subtotal
            })

            print(f"Agregado: {cantidad_vender} x {producto.nombre} = ${subtotal:.2f}")

        except Exception as e:
            print("Error al procesar el producto")
            print(e)
            continue

        continuar = input("\n¿Desea agregar otro producto a la venta? (s/n): ")
        if continuar.lower() != "s":
            seguir_agregando = False

    if not productos_vendidos:
        print("No se agregó ningún producto. Venta cancelada.")
        return

    nombre_venta = input("\nEscriba un nombre/referencia para esta venta: ")
    fecha_venta = date.today()

    try:
        venta = Venta(
            id_venta=None,
            nombre_venta=nombre_venta,
            usuario_id=None,
            ganancia=ganancia_total,
            fecha=fecha_venta,
            articulo=productos_vendidos
        )

        venta_dao.insertar(venta)
        print(f"\nVenta registrada correctamente. Total: ${ganancia_total:.2f}")

        mostrar_ticket(nombre_venta, fecha_venta, detalle_ticket, ganancia_total)

    except Exception as e:
        print("Error al registrar la venta")
        print(e)

def mostrar_ticket(nombre_venta, fecha_venta, detalle_ticket, ganancia_total):
    print("\n" + "=" * 45)
    print("           Stockex - Ticket de Venta")
    print("=" * 45)
    print(f"Venta: {nombre_venta}")
    print(f"Fecha: {fecha_venta}")
    print("-" * 45)
    print(f"{'Producto':<20}{'Cant.':<6}{'P.Unit':<9}{'Subtotal'}")
    print("-" * 45)

    for item in detalle_ticket:
        print(f"{item['nombre']:<20}{item['cantidad']:<6}"
              f"${item['precio_unitario']:<8.2f}${item['subtotal']:.2f}")

    print("-" * 45)
    print(f"{'TOTAL:':<35}${ganancia_total:.2f}")
    print("=" * 45)

def reporte_ventas():
    print("\n----------- Reporte de Ventas -----------")

    fecha_inicio_str = input("Escriba la fecha de inicio (YYYY-MM-DD): ")
    fecha_fin_str = input("Escriba la fecha final (deje vacío para usar la fecha actual): ")

    try:
        fecha_inicio = date.fromisoformat(fecha_inicio_str)

        if fecha_fin_str.strip() == "":
            fecha_fin = date.today()
        else:
            fecha_fin = date.fromisoformat(fecha_fin_str)

            if fecha_fin > date.today():
                print("Error: la fecha final no puede ser posterior a la fecha actual.")
                return

        if fecha_inicio > fecha_fin:
            print("Error: la fecha de inicio no puede ser posterior a la fecha final.")
            return

        ruta_pdf = generar_reporte_ventas_pdf(fecha_inicio, fecha_fin)

        if ruta_pdf:
            print(f"\nReporte generado correctamente en: {ruta_pdf}")

    except ValueError:
        print("Formato de fecha inválido. Use YYYY-MM-DD.")
    except Exception as e:
        print("Error al generar el reporte")
        print(e)

def main():
    
        print("\n--- Menú de Productos ---")
        print("1. Insertar producto")
        print("2. Ver productos")
        print("3. Actualzar producto")
        print("4. Eliminar producto")
        print("5. Insertar proveedor")
        print("6. Ver proveedores")
        print("7. Actualizar proveedor")
        print("8. Eliminar proveedor")
        print("9. Insetar categoria")
        print("10. Ver categorias")
        print("11. Actualizar categoria")
        print("12. Eliminar categoria")
        print("13. Registrar venta")
        print("14. Generar reporte")
            
        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                insertar_producto()
            case 2:
                ver_productos()
            case 3:
                actualizar_producto()
            case 4:
                eliminar_producto()
            case 5:
                insertar_proveedor()
            case 6:    
                ver_proveedores()
            case 7:
                actualizar_proveedor()
            case 8:
                eliminar_proveedor()
            case 9:
                insertar_categoria()
            case 10:
                ver_categorias()
            case 11:
                actualizar_categoria()
            case 12:
                eliminar_categoria
            case 13:
                registrar_venta()
            case 14:
                reporte_ventas()

if __name__ == "__main__":
    main()