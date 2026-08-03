from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import date
from collections import Counter
import os

from dao.venta_dao import VentaDAO
from dao.producto_dao import ProductoDAO

def generar_reporte_ventas_pdf(fecha_inicio, fecha_fin):
    venta_dao = VentaDAO()
    producto_dao = ProductoDAO()

    ventas = venta_dao.obtener_por_rango_fechas(fecha_inicio, fecha_fin)

    if not ventas:
        print(f"No se encontraron ventas entre {fecha_inicio} y {fecha_fin}.")
        return None

    # ---- Cálculos del resumen ----
    total_ventas = len(ventas)
    ganancia_total = sum(float(venta.ganancia) for venta in ventas)
    promedio_venta = ganancia_total / total_ventas

    contador_productos = Counter()
    for venta in ventas:
        for id_producto in venta.articulo:
            contador_productos[id_producto] += 1

    productos_top = contador_productos.most_common(5)

    # ---- Generar PDF ----
    carpeta_reportes = "reportes"
    os.makedirs(carpeta_reportes, exist_ok=True)

    nombre_archivo = f"reporte_ventas_{fecha_inicio}_a_{fecha_fin}.pdf"
    ruta_completa = os.path.join(carpeta_reportes, nombre_archivo)

    c = canvas.Canvas(ruta_completa, pagesize=letter)
    ancho, alto = letter
    y = alto - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(40, y, "Reporte de Ventas")
    y -= 20

    c.setFont("Helvetica", 10)
    c.drawString(40, y, f"Periodo: {fecha_inicio} a {fecha_fin}")
    y -= 15
    c.drawString(40, y, f"Generado el: {date.today()}")
    y -= 30

    c.setFont("Helvetica-Bold", 13)
    c.drawString(40, y, "Resumen General")
    y -= 20

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Número de ventas: {total_ventas}")
    y -= 15
    c.drawString(50, y, f"Ganancia total: ${ganancia_total:.2f}")
    y -= 15
    c.drawString(50, y, f"Promedio por venta: ${promedio_venta:.2f}")
    y -= 30

    c.setFont("Helvetica-Bold", 13)
    c.drawString(40, y, "Productos Más Vendidos")
    y -= 20

    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y, "Producto")
    c.drawString(350, y, "Veces vendido")
    y -= 5
    c.line(40, y, 550, y)
    y -= 15

    c.setFont("Helvetica", 10)
    if productos_top:
        for id_producto, veces in productos_top:
            producto = producto_dao.obtener_por_id(id_producto)
            nombre = producto.nombre if producto else f"(ID {id_producto} eliminado)"
            c.drawString(50, y, nombre)
            c.drawString(350, y, str(veces))
            y -= 15
    else:
        c.drawString(50, y, "Sin datos.")
        y -= 15

    y -= 20

    c.setFont("Helvetica-Bold", 13)
    c.drawString(40, y, "Detalle de Ventas")
    y -= 20

    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, y, "ID")
    c.drawString(90, y, "Nombre")
    c.drawString(280, y, "Fecha")
    c.drawString(380, y, "Ganancia")
    y -= 5
    c.line(40, y, 550, y)
    y -= 15

    c.setFont("Helvetica", 10)
    for venta in ventas:
        if y < 60:
            c.showPage()
            y = alto - 50
            c.setFont("Helvetica", 10)

        c.drawString(50, y, str(venta.id_venta))
        c.drawString(90, y, venta.nombre_venta[:30])
        c.drawString(280, y, str(venta.fecha))
        c.drawString(380, y, f"${float(venta.ganancia):.2f}")
        y -= 15

    c.save()
    return ruta_completa