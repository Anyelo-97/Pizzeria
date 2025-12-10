from utils.jsonFIleHandler import readFile, saveFile
from utils.limpiarConsola import limpiarConsola
from resources.autoCode import autoCodePD  
from utils.path import PRODUCT_FILE_PATH
from datetime import datetime
from tabulate import tabulate


#   AGREGAR PRODUCTO

def addProduct():
    limpiarConsola()
    productos = readFile(PRODUCT_FILE_PATH) or []

    print("=== AGREGAR PRODUCTO ===")

    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return
    
    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
    except ValueError:
        print("Precio o stock inválido.")
        return

    producto = {
        "code": autoCodePD(),
        "name": nombre,
        "price": precio,
        "stock": stock,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    productos.append(producto)
    saveFile(PRODUCT_FILE_PATH, productos)

    print("Producto agregado con éxito.")



#   MOSTRAR PRODUCTOS

def showProducts():
    limpiarConsola()
    productos = readFile(PRODUCT_FILE_PATH) or []

    print("=== LISTA DE PRODUCTOS ===")

    if not productos:
        print("No hay productos registrados.")
        return

    table = [
        [
            p["codigo"],
            p["nombre"],
            p["precio"],
            p["stock"],
            p["fecha"]
        ]
        for p in productos
    ]

    headers = ["Código", "Nombre", "Precio", "Stock", "Fecha"]
    print(tabulate(table, headers, tablefmt="simple_grid"))



#   EDITAR PRODUCTO

def editProduct():
    showProducts()
    productos = readFile(PRODUCT_FILE_PATH) or []

    codigo = input("\nIngrese el código del producto a editar: ")

    for p in productos:
        if p["codigo"] == codigo:
            print(f"Editando {p['nombre']}")

            nuevo_nombre = input(f"Nuevo nombre ({p['nombre']}): ").strip()
            nuevo_precio = input(f"Nuevo precio ({p['precio']}): ").strip()
            nuevo_stock = input(f"Nuevo stock ({p['stock']}): ").strip()

            if nuevo_nombre:
                p["nombre"] = nuevo_nombre
            if nuevo_precio:
                p["precio"] = float(nuevo_precio)
            if nuevo_stock:
                p["stock"] = int(nuevo_stock)

            saveFile(PRODUCT_FILE_PATH, productos)
            print("Producto actualizado.")
            return

    print("Código no encontrado.")



#   ELIMINAR PRODUCTO

def deleteProduct():
    showProducts()
    productos = readFile(PRODUCT_FILE_PATH) or []

    codigo = input("\nCódigo del producto a eliminar: ")

    for p in productos:
        if p["codigo"] == codigo:
            productos.remove(p)
            saveFile(PRODUCT_FILE_PATH, productos)
            print("Producto eliminado.")
            return

    print("Código no encontrado.")



#   BUSCAR PRODUCTO

def searchProduct():
    productos = readFile(PRODUCT_FILE_PATH) or []
    texto = input("Buscar por nombre o código: ").lower()

    encontrados = [
        p for p in productos
        if texto in p["nombre"].lower() or texto in p["codigo"].lower()
    ]

    if not encontrados:
        print("No se encontraron coincidencias.")
        return

    print("=== RESULTADOS ===")
    table = [
        [p["codigo"], p["nombre"], p["precio"], p["stock"], p["fecha"]]
        for p in encontrados
    ]

    headers = ["Código", "Nombre", "Precio", "Stock", "Fecha"]
    print(tabulate(table, headers, tablefmt="simple_grid"))
