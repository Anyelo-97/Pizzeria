from utils.jsonFIleHandler import *
from resources.autoCode import *
from utils.path import PRODUCT_FILE_PATH
from datetime import *
from utils.limpiarConsola import *

# Funcion para agregar nuevos productos al JSON
def addElement():
    products = readFile(PRODUCT_FILE_PATH)
    limpiarConsola()
    print("=== A G R E G A R  P R O D U C T O ===")
    
    # Solicitar datos y guardarlos en una variable
    code = autoCodePD()
    name = input("Ingrese el nombre ")
    category = input("Ingrese el categoria ")
    price = int(input("Ingrese el precio "))
    desc = input("¿Desea agregar una descripcion? s/n ")
    
    # Desicion para añadir descripción, por defecto queda vacio
    if desc == "s":
        description = input("Ingrese una descripción ")
    elif desc == "n": description = ("")
    
    # Establecer fecha especifica o la fecha local 
    dateif = input("¿Desea agregar una fecha diferente a la de hoy? s/n ")
    if dateif == "s":
        year = int(input('Ingresa el año '))
        month = int(input('Ingrese el mes '))
        day = int(input('Ingresa el dia '))
        dates = datetime.date(year, month, day)
        date = dates.isoformat()
    elif dateif =="n":
        date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    
    # Guardar los datos en una lista
    newProduct = {"code": code,
                  "name": name, 
                  "category": category,
                  "price": price,
                  "description": description,
                  "date": date
                }
    
    # Agregar los datos del producto al JSON
    products.append(newProduct)
    
    # Guardar los datos agregados al JSON
    saveFile(PRODUCT_FILE_PATH, products)
