from utils.path import *
from datetime import *
from utils.jsonFIleHandler import *
from resources.autoCode import *
from utils.limpiarConsola import *

def addClient():
    client = readFile(CLIENT_FILE_PATH)
    limpiarConsola()

    print("====================================")
    print("  D A T O S  D E L  C L I E N T E")
    print("====================================")
    
    name = input("Ingrese el nombre ")
    id = int(input("Ingrese el número de documento "))
    phone = int(input("Télefo del cliente "))
    cdClient = autoCodeCL()
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M") 
    
    newClient ={
        "Número de documuento del cliente": id,
        "Nombre del cliente": name,
        "Télefono del cliente": phone,
        "Fecha de registro": fecha
    }
    
    # Agregar los datos del producto al JSON
    client.append(newClient)
    
    # Guardar los datos agregados al JSON
    saveFile(CLIENT_FILE_PATH, client)
    
    return