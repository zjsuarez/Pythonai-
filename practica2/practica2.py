import json
import os

horarios = {
    
}


 
 
def menu():
    global horarios
    try:
        # Obtener la ruta absoluta del script actual
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(script_dir, 'horarios.json')

        with open(json_path, encoding='utf-8') as f:
            horarios = json.load(f)
        print("Archivo cargado correctamente.")
    except Exception as e:
        print(f"Error al cargar horarios: {e}")

        
    """
    Menú principal repetitivo (bucle while) para elegir acciones:
      1) Mostrar registros
      2) Contar entradas
      3) Salir
    """
    while True:
        print("========== MENÚ ==========")
        print("1) Mostrar registros")
        print("2) Contar entradas")
        print("3) Salir")
        opcion = input("Elige una opción (1-3): ").strip()
 
        if opcion == '1':
            mostrar_registros()
        elif opcion == '2':
            contar_entradas()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")
 
def mostrar_registros():
    for i in enumerate(horarios.items(), start=1):
        print(i)


def contar_entradas():
    try:
        inputuser = input("Introduce la hora (horas:minutos): ")
        hora = inputuser.split(":")
        if int(hora[0]) < 0 or int(hora[0]) > 23:
            print("Hora inválida. La hora debe estar entre 0 y 23")
            return
        if int(hora[1]) < 0 or int(hora[1]) > 59:
            print("Hora inválida. Los minutos deben de estar entre 0 y 59")
    except ValueError:
        print("Debes introducir un número entero")
        return

    count = 0

    for nombre, (entrada, salida) in horarios.items():
        if int(horas_a_minutos(entrada)) <= horas_a_minutos(inputuser):
            count=count+1
    

    print("Personas trabajando:", count)
        
def horas_a_minutos(horastr):
    hora = horastr.split(":")

    return int(hora[0])*60 + int(hora[1])

# ---------------------------------------------------------------------------
# 4) Punto de entrada
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # Consejo de depuración: descomenta las dos líneas siguientes para pausar en este punto
    # import debugpy
    # debugpy.breakpoint()
    menu()



