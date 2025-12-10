from utils.jsonFIleHandler import *
from utils.findDictionaryIndex import *
from utils.path import *

def autoCodePD():
    products = readFile(PRODUCT_FILE_PATH)

    # Recorre el contenido dentro del JSON, y si esta vacio lo establece en 1 
    if len(products) == 0:
        return 1
    
    # Auto incrementar el valor de "code", sumando 1 al valor existente anterior
    last_code = max(int(p["code"]) for p in products)
    return last_code + 1

def autoCodeCL():
    client = readFile(CLIENT_FILE_PATH)

    if len(client) == 0:
        return 1
    

    last_code = max(int(p["code"]) for p in client)
    return last_code + 1


def autoCodeOD():
    orders = readFile(ORDER_FILE_PATH)

    if len(orders) == 0:
        return 1
    
    
    last_code = max(int(p["code"]) for p in orders)
    return last_code + 1

