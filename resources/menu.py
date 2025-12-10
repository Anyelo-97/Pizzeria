from utils.limpiarConsola import limpiarConsola
from resources.products import addProduct, showProducts, editProduct, deleteProduct, searchProduct

def menu(optionsmenu=None):
    limpiarConsola()
    optionsmenu = (
        "Agregar producto",
        "Mostrar productos",
        "Editar producto",
        "Eliminar producto",
        "Buscar producto",
        "Salir"
    )

    while True:
        index = 1
        
        for item in optionsmenu:
            print(f"{index}. {item}")
            index += 1

        try:
            choisePD = int(input("\nIngrese la opción: "))
        except ValueError:
            print("Debe ser un número.")
            continue

        match choisePD:
            case 1:
                addProduct()
            case 2:
                showProducts()
            case 3:
                editProduct()
            case 4:
                deleteProduct()
            case 5:
                searchProduct()
            case 6:
                print("Saliendo...")
                break

        input("\nPresione ENTER para continuar...")
        limpiarConsola()
