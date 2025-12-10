from resources.addClient import *
from resources.menu import *
from resources.orders import *
from utils.limpiarConsola import *

while True:
    limpiarConsola()
    # Imprimir titulo por defecto
    print("===============================")
    print(" ====== P I Z Z E R I A ======")
    print("===============================")
    
    print("\n1. Agregar productos ")
    print("2. Armar pedidos ")
    print("3. Clientes ")
    print("4. Salir")

    try:
        choise = int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Opción inválida. Intente de nuevo.")
        input("Presione Enter para continuar...")
        continue

    match choise:
        case 1:
            menu()
        case 2:
            orders()
        case 3:
            addClient()
        case 4:
            print("Saliendo...")
            break
        case _:
            print("Opción no reconocida.")
    

