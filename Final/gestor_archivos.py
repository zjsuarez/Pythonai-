import csv
import os
import sys
from datetime import datetime, date
from cliente import *
from venta import *
from evento import *


# ---------------------------------------------
# ---------------- CARGAR DATOS
# ---------------------------------------------

def cargar_datos():

   #RUTAS 

    script_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_data_absoluta = os.path.join(script_dir, "data")
    
    
    #CARGAR los archivos csv de datos y convertirlos en objetos en colecciones.
    
    clientes_db = {}
    eventos_db = {}
    ventas_db = []

    print("Iniciando carga de datos...")
    
    try:
        # --- Cargar Clientes ---
        ruta_clientes = os.path.join(ruta_data_absoluta, "clientes.csv")
        with open(ruta_clientes, mode='r', newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f, delimiter=';')
            for fila in lector:
                cliente = Cliente(
                    fila['id_cliente'],
                    fila['nombre'],
                    fila['email'],
                    fila['fecha_registro']
                )
                clientes_db[cliente.id_cliente] = cliente

        # --- Cargar Eventos ---
        ruta_eventos = os.path.join(ruta_data_absoluta, "eventos.csv")
        with open(ruta_eventos, mode='r', newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f, delimiter=';')
            for fila in lector:
                evento = Evento(
                    fila['id_evento'],
                    fila['nombre'],
                    fila['fecha'],
                    fila['precio'],
                    fila['categoria']
                )
                eventos_db[evento.id_evento] = evento

        # --- Cargar Ventas ---
        ruta_ventas = os.path.join(ruta_data_absoluta, "ventas.csv")
        with open(ruta_ventas, mode='r', newline='', encoding='utf-8') as f:
            lector = csv.DictReader(f, delimiter=';')
            for fila in lector:
                venta = Venta(
                    fila['id_venta'],
                    fila['id_cliente'],
                    fila['id_evento'],
                    fila['fecha_venta']
                )
                ventas_db.append(venta)
        
        print(f"Carga completada: {len(clientes_db)} clientes, {len(eventos_db)} eventos, {len(ventas_db)} ventas.")
        return clientes_db, eventos_db, ventas_db

    except Exception as e:
        print(f"Error: {e}")
        
        
# ---------------------------------------------
# ---------------- LISTAR DATOS
# ---------------------------------------------

def listar_datos(coleccion_datos, titulo: str):
    print(f"\n--- Listado de {titulo} ---")
    
    if not coleccion_datos:
        print(f"No hay {titulo.lower()} para mostrar.")
        return

    if isinstance(coleccion_datos, dict):
        for item in coleccion_datos.values():
            print(item)
    else:
        for item in coleccion_datos:
            print(item)
            
            
            
            
# ---------------------------------------------
# ---------------- ALTA CLIENTE
# ---------------------------------------------
        
def alta_cliente(clientes_db: dict):
    print("\n--- Alta de Nuevo Cliente ---")
    

    nombre = input("Nombre del cliente: ")
    if not nombre:
        print("Error: El nombre no puede estar vacío.")
        return # VALIDAR ERRORES

    email = input("Email del cliente: ")
    if not validar_email(email):
        print("Error: El formato del email no es válido (debe tener '@' y '.').") #VALIDAR EL CORREO!
        return 

    nuevo_id = generar_nuevo_id_cliente(clientes_db)
    fecha_registro_obj = date.today() 
    fecha_registro_str = fecha_registro_obj.strftime('%Y-%m-%d')

    try:
        nuevo_cliente = Cliente(nuevo_id, nombre, email, fecha_registro_str)
    except Exception as e:
        print(f"Error al crear el objeto cliente (revisa los datos): {e}")
        return


    try:

        script_dir = os.path.dirname(os.path.abspath(__file__))
        ruta_data_absoluta = os.path.join(script_dir, "data")
        ruta_clientes = os.path.join(ruta_data_absoluta, "clientes.csv")


        with open(ruta_clientes, mode='a', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            

            escritor.writerow([
                nuevo_cliente.id_cliente, 
                nuevo_cliente.nombre, 
                nuevo_cliente.email, 
                fecha_registro_str
            ])
        
        clientes_db[nuevo_id] = nuevo_cliente
        
        print(f"¡Cliente guardado con éxito!")
        print(nuevo_cliente)

    except Exception as e:
        print(f"Error: {e}")
        
        
# ---------------------------------------------
# ---------------- VALIDACIONES
# ---------------------------------------------        
        

# VALIDAR EMAIL
def validar_email(email: str) -> bool:
    return '@' in email and '.' in email

# GENERAR ID
def generar_nuevo_id_cliente(clientes_db: dict) -> str:
    nuevo_numero = len(clientes_db) + 1
    nuevo_id = f"c{nuevo_numero:03d}"
    return nuevo_id
        
        
        
# ---------------------------------------------
# ---------------- FILTRAR VENTAS
# ---------------------------------------------        

def filtrar_ventas_por_rango(ventas_db: list):
    print("\n--- Filtrar Ventas por Rango de Fechas ---")
    
    # Pedir fecha inicio
    fecha_inicio_str = input("Introduzca la FECHA INICIO (YYYY-MM-DD): ")
    try:
        # Validar fecha creando un objeto, si el objeto no se puede crear la fecha es invalida B)
        fecha_inicio_obj = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date()
    except ValueError:
        print("Error: Formato de fecha de inicio incorrecto. Use YYYY-MM-DD.")
        return

    # Pedir fecha final
    fecha_fin_str = input("Introduzca la FECHA FIN (YYYY-MM-DD): ")
    try:
        # Pues basicamente lo mismo de fecha de inicio 
        fecha_fin_obj = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date()
    except ValueError:
        print("Error: Formato de fecha de fin incorrecto. Use YYYY-MM-DD.")
        return

    # Obviamente validar que la fecha de inicio no se aposterior a la fecha de fin
    if fecha_inicio_obj > fecha_fin_obj:
        print("Error: La fecha de inicio no puede ser posterior a la fecha de fin.")
        return
        
    # Crear la lista
    ventas_filtradas = []
    for venta in ventas_db:
        if fecha_inicio_obj <= venta.fecha_venta <= fecha_fin_obj:
            ventas_filtradas.append(venta)

    # Mostrar resultados
    if ventas_filtradas:
        print(f"\nSe encontraron {len(ventas_filtradas)} ventas entre {fecha_inicio_str} y {fecha_fin_str}:")
        # Reutilizo el metodo de antes pa mostrar los datos
        listar_datos(ventas_filtradas, "Ventas Filtradas") 
        
# ---------------------------------------------
# ---------------- ESTADÍSTICAS
# ---------------------------------------------       
        
def estadisticas(eventos_db: dict, ventas_db: list):
    print("\n--- Estadísticas y Métricas ---")
    
    # Variables
    ingresos_totales = 0.0
    ingresos_por_evento = {}
    categorias_existentes = set() 
    precios_eventos = [] 


    for venta in ventas_db:
        evento = eventos_db.get(venta.id_evento)
        
        if evento:
            precio_evento = evento.precio
            ingresos_totales += precio_evento
            

            ingresos_por_evento.setdefault(evento.nombre, 0.0)
            ingresos_por_evento[evento.nombre] += precio_evento
            
            categorias_existentes.add(evento.categoria)
    
            if evento.precio not in precios_eventos:
                 precios_eventos.append(precio_evento)
    
    hoy = date.today()
    dias_minimo = float('inf') 
    evento_proximo = None

    for evento in eventos_db.values():
        dias_faltantes = evento.dias_hasta_evento() 
        
        if dias_faltantes > 0 and dias_faltantes < dias_minimo:
            dias_minimo = dias_faltantes
            evento_proximo = evento.nombre
    
    precio_min = min(precios_eventos) if precios_eventos else 0.0
    precio_max = max(precios_eventos) if precios_eventos else 0.0
    precio_media = sum(precios_eventos) / len(precios_eventos) if precios_eventos else 0.0

    tupla_precios = (precio_min, precio_max, precio_media)

    print(f"1. Ingresos Totales: {ingresos_totales:.2f}€")   
    print("2. Ingresos por Evento:")
    for nombre_evento, total in ingresos_por_evento.items():
        print(f"   - {nombre_evento}: {total:.2f}€")

    print(f"3. Categorías Existentes: {categorias_existentes}")
    
    if evento_proximo:
        print(f"4. Próximo evento: ({evento_proximo}) en {dias_minimo} días.")
    else:
        print("4. No hay eventos futuros programados.")
    print(f"5. Tupla de Precios (Min, Max, Media): ({tupla_precios[0]:.2f}€, {tupla_precios[1]:.2f}€, {tupla_precios[2]:.2f}€)")
        
        
# ---------------------------------------------
# ---------------- EXPORTAR INFORME
# ---------------------------------------------     
        
        
def exportar_informe(eventos_db: dict, ventas_db: list):
    print("\n--- Exportando Informe de Resumen ---")
    
        
    # Calcular Ingresos por Evento
    ingresos_por_evento = {} 
    
    for venta in ventas_db:
        evento = eventos_db.get(venta.id_evento)
        
        if evento:
            precio_evento = evento.precio

            # Acumulo los ingresos.
            ingresos_por_evento.setdefault(evento.id_evento, 0.0)
            ingresos_por_evento[evento.id_evento] += precio_evento


    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        nombre_archivo = "informe_resumen.csv"
        ruta_informe = os.path.join(script_dir, nombre_archivo)

        with open(ruta_informe, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            
            # CABECERA
            escritor.writerow(['ID_EVENTO', 'NOMBRE_EVENTO', 'INGRESOS_TOTALES'])
            
            # Escribir los datos por evento
            for id_evento, total_ingresos in ingresos_por_evento.items():
                
                # Buscamos el nombre del evento para que el informe sea más útil
                nombre_evento = eventos_db.get(id_evento).nombre if eventos_db.get(id_evento) else "Desconocido"
                
                escritor.writerow([
                    id_evento,
                    nombre_evento,
                    f"{total_ingresos:.2f}" # Formatear el float a string con 2 decimales
                ])
        
        print(f"¡Informe generado!")

    except Exception as e:
        print(f"Error: {e}")