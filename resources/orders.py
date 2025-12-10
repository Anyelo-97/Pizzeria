from utils.path import *
from utils.limpiarConsola import *
from utils.jsonFIleHandler import *
from datetime import *
from resources.autoCode import *
from tabulate import *

def orders():
    limpiarConsola()
    
    # Cargar datos
    orders = readFile(ORDER_FILE_PATH) or []
    products = readFile(PRODUCT_FILE_PATH) or []

    date = datetime.now().strftime("%d/%m/%Y %H:%M")
    code = autoCodeOD()

    order = {
        "code": code,
        "date": date,
        "detalle": [],  
        "total": 0
    }

    print("=== CREAR NUEVA ORDEN ===")
    print("Ingrese productos. Escriba '0' para finalizar.\n")

    # BUCLÉ PARA AGREGAR PRODUCTOS  
    while True:
        product_name = input("Producto: ").strip()

        if product_name == "0":
            break

        # Buscar producto
        found = None
        for p in products:
            if p["name"].lower() == product_name.lower():
                found = p
                break

        if not found:
            print("Producto no encontrado.")
            continue

        # Cantidad
        try:
            qty = int(input("Cantidad: "))
            if qty <= 0:
                print("La cantidad debe ser mayor a 0.")
                continue
        except ValueError:
            print("La cantidad debe ser un número.")
            continue

        # Validar stock
        if qty > found["stock"]:
            print(f"Stock insuficiente. Disponible: {found['stock']}")
            continue

        # Restar stock
        found["stock"] -= qty

        # Registrar detalle
        subtotal = found["price"] * qty

        order["detalle"].append({
            "name": found["name"],
            "qty": qty,
            "price": found["price"],
            "subtotal": subtotal
        })

        order["total"] += subtotal

        print(f"✔ Agregado: {found['name']}  x{qty}  (${subtotal})\n")

    # Validar orden vacía
    if not order["detalle"]:
        print("No se agregaron productos. No se creó la orden.")
        return

    # Guardar orden
    orders.append(order)
    saveFile(ORDER_FILE_PATH, orders)

    # Guardar cambios de stock
    saveFile(PRODUCT_FILE_PATH, products)

    # Mostrar factura
    print("\n========== FACTURA ==========")
    print(f"Orden: {order['code']}")
    print(f"Fecha: {order['date']}")
    print("------------------------------")

    for item in order["detalle"]:
        print(f"{item['name']}  x{item['qty']}  -  {item['subtotal']}")

    print("------------------------------")
    print(f"TOTAL: {order['total']}")
    print("==============================")

    input("\nPresione ENTER para continuar...")
