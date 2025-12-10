import os

def limpiarConsola():
    input("Presione cualquier tecla para continuar... \n")
    os.system("cls" if os.name == "nt" else "clear")
