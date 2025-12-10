from utils.jsonFIleHandler import readFile, saveFile
from utils.limpiarConsola import limpiarConsola
from resources.autoCode import autoCodePD  
from utils.path import PRODUCT_FILE_PATH
from datetime import datetime
from tabulate import tabulate


#   AGREGAR PRODUCTO

def addProduct():
    limpiarConsola()
    products = readFile(PRODUCT_FILE_PATH) or []

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

    products.append(producto)
    saveFile(PRODUCT_FILE_PATH, products)

    print("Producto agregado con éxito.")



#   MOSTRAR PRODUCTOS

def showProducts():
    limpiarConsola()
    products = readFile(PRODUCT_FILE_PATH) or []

    print("=== LISTA DE PRODUCTOS ===")

    if not products:
        print("No hay products registrados.")
        return

    table = [
        [
            p["code"],
            p["name"],
            p["price"],
            p["stock"],
            p["date"]
        ]
        for p in products
    ]

    headers = ["Código", "Nombre", "Precio", "Stock", "Fecha"]
    print(tabulate(table, headers, tablefmt="simple_grid"))



#   EDITAR PRODUCTO

def editProduct():
    showProducts()
    products = readFile(PRODUCT_FILE_PATH) or []

    codigo = input("\nIngrese el código del producto a editar: ")

    for p in products:
        if str(p["code"] == codigo):
            print(f"Editando {p['name']}")

            nuevo_nombre = input(f"Nuevo nombre ({p['name']}): ").strip()
            nuevo_precio = input(f"Nuevo precio ({p['price']}): ").strip()
            nuevo_stock = input(f"Nuevo stock ({p['stock']}): ").strip()

            if nuevo_nombre:
                p["name"] = nuevo_nombre
            if nuevo_precio:
                p["price"] = float(nuevo_precio)
            if nuevo_stock:
                p["stock"] = int(nuevo_stock)

            saveFile(PRODUCT_FILE_PATH, products)
            print("Producto actualizado.")
            return

    print("Código no encontrado.")



#   ELIMINAR PRODUCTO

def deleteProduct():
    showProducts()
    products = readFile(PRODUCT_FILE_PATH) or []

    codigo = input("\nCódigo del producto a eliminar: ")

    for p in products:
        if p["code"] == codigo:
            products.remove(p)
            saveFile(PRODUCT_FILE_PATH, products)
            print("Producto eliminado.")
            return

    print("Código no encontrado.")



#   BUSCAR PRODUCTO

def searchProduct():
    products = readFile(PRODUCT_FILE_PATH) or []
    texto = input("Buscar por nombre o código: ").lower()

    encontrados = [
        p for p in products
        if texto in p["name"].lower() or texto in p["code"].lower()
    ]

    if not encontrados:
        print("No se encontraron coincidencias.")
        return

    print("=== RESULTADOS ===")
    table = [
        [p["code"], p["name"], p["price"], p["stock"], p["date"]]
        for p in encontrados
    ]

    headers = ["Código", "Nombre", "Precio", "Stock", "Fecha"]
    print(tabulate(table, headers, tablefmt="simple_grid"))
