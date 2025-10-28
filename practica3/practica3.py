import csv
import os


# -------------------------------------------------------------------
# --------------------- CLASE REGISTRO HORARIO ----------------------
# -------------------------------------------------------------------

class RegistroHorario:
    def __init__(self, empleado: str, dia: str, entrada: int, salida: int):
        self.empleado = empleado
        self.dia = dia
        self.entrada = entrada
        self.salida = salida

    def duracion(self) -> int:
        """Devuelve la cantidad de horas trabajadas en este registro"""
        if self.salida <= self.entrada:
            # Turno de noche
            return (24 - self.entrada) + self.salida
        else:
            # Turno normal
            return self.salida - self.entrada
    
    
# -------------------------------------------------------------------
# ------------------------- CLASE EMPLEADO --------------------------
# -------------------------------------------------------------------
class Empleado:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.registros = [] 

    def agregar_registro(self, registro: RegistroHorario):
        self.registros.append(registro)

    def horas_totales(self) -> int:
        return sum(r.duracion() for r in self.registros)

    def dias_trabajados(self) -> int:
        dias_unicos = {r.dia for r in self.registros}
        return len(dias_unicos)

    def fila_csv(self) -> list:
        return [self.nombre, self.dias_trabajados(), self.horas_totales()]

# -------------------------------------------------------------------
# --------------------- CLASE GESTOR HORARIOS -----------------------
# -------------------------------------------------------------------


class GestorHorarios:
    def __init__(self, archivo_entrada: str):
        self.archivo_entrada = archivo_entrada
        self.empleados = {} 

    def leer_y_agrupar_registros(self):
        print(f"\nLeyendo {self.archivo_entrada} y agrupando por clases...")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_csv = os.path.join(script_dir, self.archivo_entrada)
        try:
            with open(ruta_csv, newline='', encoding='utf-8') as f:
                lector = csv.reader(f, delimiter=';', quotechar='"')
                
                for fila in lector:

                    nombre, dia, h_entrada, h_salida = fila
                    registro = RegistroHorario(nombre, dia, int(h_entrada), int(h_salida))


                    if nombre not in self.empleados:
                        self.empleados[nombre] = Empleado(nombre)
                    
                    # 2. Se añade el registro al objeto Empleado correspondiente
                    self.empleados[nombre].agregar_registro(registro)
            
            print(f"Agrupación completada: {len(self.empleados)} empleados en total.")

        except Exception as e:
            print("Error")


    def escribir_resumen_clases(self, archivo_salida: str):
        print(f"Escribiendo resumen en '{archivo_salida}'...")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_salida = os.path.join(script_dir, archivo_salida)

        try:
            with open(ruta_salida, 'w', newline='', encoding='utf-8') as f:
                escritor = csv.writer(f, delimiter=';')
                escritor.writerow(['Empleado', 'Dias_Trabajados', 'Horas_Totales'])
                
                for empleado_obj in self.empleados.values():
                    escritor.writerow(empleado_obj.fila_csv())
            
            print(f"Se generó el fichero {archivo_salida}")
            
        except Exception as e:
            print("Error")

# -------------------------------------------------------------------
# --------------------- CARGAR LISTA REGISTROS ----------------------
# -------------------------------------------------------------------

#INICIALIZO VARIABLE REGISTRO PARA PODER USARLO EN OTRAS FUNCIONES    
registros = []


script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'horarios.csv')

with open(csv_path, newline='', encoding='utf-8') as f:
    lector = csv.reader(f, delimiter=';', quotechar='"')
    for fila in lector:
        # Cada fila es una lista de cadenas: [nombre, dia, entrada, salida]
        nombre, dia, h_entrada, h_salida = fila
        # Convertimos las horas a enteros
        entrada = int(h_entrada)
        salida = int(h_salida)
        registro = RegistroHorario(nombre, dia, entrada, salida)
        registros.append(registro)
print(f"Se han leído {len(registros)} registros")

# -------------------------------------------------------------------
# -------------------- CARGAR EMPELADOS POR DIA ---------------------
# -------------------------------------------------------------------


empleados_por_dia = {}
for registro in registros:
    # Creamos el conjunto para el día si no existe
    if registro.dia not in empleados_por_dia:
        empleados_por_dia[registro.dia] = set()
    # Añadimos el empleado al conjunto del día
    empleados_por_dia[registro.dia].add(registro.empleado)

# Mostrar empleados por día
for dia, empleados in empleados_por_dia.items():
    print(f"{dia}: {empleados}")

# -------------------------------------------------------------------
# ----------------------- RESUMEN  HORARIOS -------------------------
# -------------------------------------------------------------------

# Calcular horas totales por empleado
horas_totales = {}
for registro in registros:
    horas_totales.setdefault(registro.empleado, 0)
    horas_totales[registro.empleado] += registro.duracion()

# Escribir un resumen en un nuevo CSV

csv_path_exit = os.path.join(script_dir, 'resumen_horarios.csv')

with open(csv_path_exit, 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # Cabecera
    escritor.writerow(['Empleado', 'Horas totales'])
    # Filas con los datos acumulados
    for empleado, total in horas_totales.items():
        escritor.writerow([empleado, total])

print("Se ha generado el fichero resumen_horarios.csv")


# -------------------------------------------------------------------
# -------------------------- Ejercicio 6.1 --------------------------
# -------------------------------------------------------------------
hora_referencia = 9

print("Buscando madrugadores...")

#INICIALIZO VARIABLE CON SET PARA EVITAR DUPLICADOS
madrugadores = set()


for registro in registros:
    if registro.entrada < hora_referencia:
        #AÑADO A LA LISTA SI ENTRÓ ANTES DE LA HORA DE REFERENCIA
        madrugadores.add( (registro.empleado, registro.entrada) )

# GUARDAMOS EN UN ARCHIVO
try:
    madrugadores_path_exit = os.path.join(script_dir, 'madrugadores.csv')
    
    with open(madrugadores_path_exit, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';')
        
        escritor.writerow(['Empleado', 'Hora_Entrada'])

        escritor.writerows(list(madrugadores)) 

    print("Se generó madrugadores.csv")

except Exception as e:
    print("Error")
# -------------------------------------------------------------------
# -------------------------- Ejercicio 6.2 --------------------------
# -------------------------------------------------------------------
print("Calculando empleados que trabajaron lunes y viernes...")

# USAMOS INTERSECCION CON & PARA OBTENER TRABAJADORES QUE ESTAN LUNES Y VIERNES
trabajaron_ambos = empleados_por_dia['Lunes'] & empleados_por_dia['Viernes']

# Mostrar por pantalla:
print(f"Empleados que trabajaron tanto lunes como viernes: {trabajaron_ambos}")

# Escribir lista en en_dos_dias.csv
try:
    # ruta salida
    ambos_dias_path_exit = os.path.join(script_dir, 'en_dos_dias.csv')
    
    with open(ambos_dias_path_exit, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';')

        
        escritor.writerow(['Empleado'])

        for empleado in list(trabajaron_ambos):
            escritor.writerow([empleado])

    print("Se generó en_dos_dias.csv")

except Exception as e:
    print(f"Error al escribir en_dos_dias.csv: {e}")
    
# -------------------------------------------------------------------
# -------------------------- Ejercicio 6.3 --------------------------
# -------------------------------------------------------------------


# Usamos - para ver trabajadoires que trabajaron un dia (sabado) pero no otro (domingo)
trabajaron_solo_sabado = empleados_por_dia['Sabado'] - empleados_por_dia['Domingo']

print("--- Empleados Exclusivos ---")
print(f"Empleados que trabajaron Sábado pero no Domingo: {trabajaron_solo_sabado}")

# -------------------------------------------------------------------
# -------------------------- Ejercicio 6.4 --------------------------
# -------------------------------------------------------------------
print("\nGenerando resumen semanal con días y horas...")

resumen_semanal = {}

for registro in registros:
    empleado = registro.empleado
    dia = registro.dia
    duracion_turno = registro.duracion()
    # Inicializo empleadois en el resumen semanal
    if empleado not in resumen_semanal:
        resumen_semanal[empleado] = {
            'horas': 0,
            'dias': set() # Uso un set para guardar los días únicos
        }
    # Acumular para total de horas
    resumen_semanal[empleado]['horas'] += duracion_turno
    # Añado el dia
    resumen_semanal[empleado]['dias'].add(dia)
# ESCRIBIR EN ARCHIVO CSV:

try:
    # RUTA
    resumen_semanal_path_exit = os.path.join(script_dir, 'resumen_semanal.csv')
    
    with open(resumen_semanal_path_exit, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        escritor.writerow(['Empleado', 'Dias_Trabajados', 'Horas_Totales'])
        

        for empleado, datos in resumen_semanal.items():
            
            # La cantidad de días trabajados es el tamaño (len) del set de días
            dias_trabajados = len(datos['dias'])
            horas_totales = datos['horas']
            
            escritor.writerow([empleado, dias_trabajados, horas_totales])

    print("Se ha generado el fichero resumen_semanal.csv")

except Exception as e:
    print("ERROR")
    
# -------------------------------------------------------------------
# -------------------------- Ejercicio 6.5 --------------------------
# -------------------------------------------------------------------

print("Buscando empleados que trabajan >= 6h en TODAS sus jornadas...")


todos_los_empleados = {registro.empleado for registro in registros}

# OBTENEMOS EMPLEADOS QUE TUVIERON UN TURNO CORTO (-6 horas)
empleados_con_turno_corto = {
    registro.empleado 
    for registro in registros 
    if registro.duracion() < 6
}


empleados_siempre_largos = todos_los_empleados - empleados_con_turno_corto

print(f"Empleados que han trabajado al menos 6h en todas sus jornadas: {empleados_siempre_largos}")

    
# -------------------------------------------------------------------
# -------------------------- Ejercicio 6.6 --------------------------
# -------------------------------------------------------------------

# 1. Crear una instancia del GestorHorarios
gestor = GestorHorarios('horarios.csv')

# 2. Ejecutar la función para leer y agrupar
gestor.leer_y_agrupar_registros()

# 3. Ejecutar la función para escribir el resumen final
gestor.escribir_resumen_clases('resumen_clases.csv')