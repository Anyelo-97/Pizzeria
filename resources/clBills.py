from resources.path import *
from utils.jsonFIleHandler import *
from resources.viewDT import *
from collections import defaultdict
from datetime import datetime

def get_week_number(date_str):

    try:
        
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return str(date_obj.isocalendar()[1]) 
    except (ValueError, TypeError):
        return None

def clBills():
    products = readFile(PRODUCT_FILE_PATH)
    viewDT()
    
    if not products:
        print("No hay productos/gastos para analizar.")
        return 0

    gastosPeriodo = []
    
    pg = input("\n¿Desea filtrar los precios por fecha? s/n ")
    
    if pg.lower() == "s":
        dateOrd = input("Ingrese la fecha que desee ordenar año(a), mes(m), semana(s), dia(d): ")
        if dateOrd == "a":
            filtrarValor = input("Ingrese el año yyyy\n")
            gastosPeriodo = [item for item in products if item.get('date','')[:4] == filtrarValor]
        elif dateOrd == "m":
            filtrarValor = input("Ingrese el mes yyyy-mm\n")
            gastosPeriodo = [item for item in products if item.get('date','')[:7] == filtrarValor]
        elif dateOrd == "s":
            filtrarValor = input("Ingrese la semana\n")
            gastosPeriodo = [item for item in products if get_week_number(item.get('date')) == filtrarValor]
        elif dateOrd == "d":
            filtrarValor = input("Ingrese el dia yyyy-mm-dd\n")
            gastosPeriodo = [item for item in products if item.get('date') == filtrarValor]
        else:
            print("Opción de período no válida. Procesando todos los gastos.")
            gastosPeriodo = products
            
        if not gastosPeriodo:
            print("No se encontraron gastos para el período especificado.")
            return 0    
            
    else: gastosPeriodo = products
    
    sumaCostos = sum(int(item['price']) for item in gastosPeriodo)
    print(f"\nGASTO TOTAL del período seleccionado: {sumaCostos}")
    
    gastosCategoria = defaultdict(int)
    for item in gastosPeriodo:
        gastosCategoria[item['category']] += int(item['price'])

    print("\n--- Gastos filtrados ---")
    
    for category, total_gasto in sorted(gastosCategoria.items(), key=lambda x: x[1], reverse=True):
        porcentaje = (total_gasto / sumaCostos) * 100
        print(f"- {category:20s}: ${total_gasto:<10} ({porcentaje:.1f}%)")

    return sumaCostos

