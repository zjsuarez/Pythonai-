import csv
import os
import sys
from datetime import datetime, date
from gestor_archivos import *


# -------------------     
# ------------------------------ MAIN
# -------------------

def main():
    """
    Función principal que ejecuta el menú en bucle.
    [Requisito: Menú de ejecución en bucle]
    """
    clientes_db, eventos_db, ventas_db = cargar_datos()
    print("\n¡Bienvenido al Mini-CRM de Eventos!")

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Listar Clientes")
        print("2. Listar Eventos")
        print("3. Listar Ventas")
        print("4. Añadir nuevo Cliente")
        print("5. Filtrar Ventas por Rango de Fechas")
        print("6. Ver Estadísticas")
        print("7. Exportar Informe de Resumen")
        print("8. Salir")
        
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == '1':
            listar_datos(clientes_db, "Clientes")
        elif opcion == '2':
            listar_datos(eventos_db, "Eventos")
        elif opcion == '3':
            listar_datos(ventas_db, "Ventas")
        elif opcion == '4':
            alta_cliente(clientes_db)
        elif opcion == '5':
            filtrar_ventas_por_rango(ventas_db)
        elif opcion == '6':
            estadisticas(eventos_db, ventas_db)
        elif opcion == '7':
            exportar_informe(eventos_db, ventas_db)
        elif opcion == '8':
            print("Gracias por usar el CRM. ¡Hasta pronto!")
            break 
        else:
            print("Opción no válida. Por favor, elija un número del 1 al 8.")



if __name__ == "__main__":
    main()