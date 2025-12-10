from utils.jsonFIleHandler import readFile
from utils.path import PRODUCT_FILE_PATH
from tabulate import tabulate
from utils.limpiarConsola import limpiarConsola

# Funcion para visualizar los datos que estan dentro del JSON
def viewDT():
    limpiarConsola()
    products = readFile(PRODUCT_FILE_PATH)
    print("=== G A S T O S  R E G I S T R A D O S === \n")
    
    # Definir un valor a la variable table, su funcionalidad es indexar los valores dentro del JSON
    table = [] 
    
    # Recorrer los valor del JSON, y almacenarlos dentro de una tupla
    for i in products:
        table.append ([
            i["code"],
            i["name"],
            f"{i['price']:,.2f}",
            i["date"]
        ])
    
    # Nombres que tendra cada columna dentro la tabla
    headers = ["code", "name", "price", "date"]
    
    # Creacion de tabla con los parametros previamente establecidos
    print(tabulate(table, headers, tablefmt="simple_grid"))
