# Práctica Final: Mini-CRM de Eventos

## 🎯 Objetivo

Desarrollar una aplicación de consola en Python para gestionar clientes, eventos y ventas a partir de ficheros CSV. El proyecto integra el manejo de archivos, clases (POO), colecciones (`list`, `dict`, `set`, `tuple`) y el módulo `datetime` para la manipulación de fechas.

## 🚀 Características Principales (Especificaciones Funcionales)

La aplicación se ejecuta en un bucle de menú interactivo que permite al usuario:

* **Cargar Datos:** Lee `clientes.csv`, `eventos.csv` y `ventas.csv` al iniciar.
* **Listar (1-3):** Muestra listados formateados de todos los clientes, eventos y ventas.
* **Alta de Cliente (4):** Añade un nuevo cliente, valida el email, genera un ID y guarda incrementalmente en `clientes.csv`.
* **Filtrar Ventas (5):** Solicita un rango de fechas (YYYY-MM-DD) y muestra solo las ventas realizadas en ese período.
* **Ver Estadísticas (6):** Calcula y muestra 5 métricas clave:
    1.  Ingresos totales.
    2.  Ingresos por evento (dict).
    3.  Set de categorías existentes.
    4.  Días hasta el evento más próximo.
    5.  Tupla (min, max, media) de precios de eventos.
* **Exportar Informe (7):** Genera un nuevo archivo `informe_ingresos_por_evento.csv` con el resumen de ingresos por cada evento.
* **Salir (8):** Cierra la aplicación.

## 🛠️ Especificaciones Técnicas (Requisitos Cumplidos)

* **Lenguaje:** Python 3
* **Módulos Estándar:** `csv` (para lectura/escritura), `os` (para rutas de archivos), `sys` (para `sys.exit`), `datetime` (para `date`, `datetime`, `timedelta`).
* **POO (Programación Orientada a Objetos):**
    * `Cliente`: Almacena datos del cliente, incluye métodos `antiguedad_dias()`.
    * `Evento`: Almacena datos del evento (convirtiendo `precio` a `float` y `fecha` a `date`), incluye método `dias_hasta_evento()`.
    * `Venta`: Almacena los datos de la transacción, convirtiendo `fecha_venta` a `date`.
    * Todas las clases incluyen métodos `__str__` para impresión formateada.
* **Gestión de Archivos:**
    * Lectura de 3 archivos CSV (`clientes.csv`, `eventos.csv`, `ventas.csv`) usando `csv.DictReader` al inicio.
    * Escritura incremental (modo 'a') para `alta_cliente()` usando `csv.writer`.
    * Escritura de reporte (modo 'w') para `exportar_informe()` usando `csv.writer`.
* **Colecciones:**
    * `dict`: Para `clientes_db` y `eventos_db` (acceso rápido por ID).
    * `list`: Para `ventas_db` y resultados filtrados.
    * `set`: Para el cálculo de categorías únicas en las estadísticas.
    * `tuple`: Para el resumen de precios (min, max, media).
* **Validaciones:**
    * Validación simple de email (`@` y `.`) en el alta.
    * Generación de nuevos IDs para clientes basado en el conteo (`len`).
    * Validación de formato de fecha (YYYY-MM-DD) usando `try-except ValueError` en el filtro de ventas.
    * Manejo de `FileNotFoundError` en la carga de datos.
* **Pruebas (Opcional):**
    * Se incluye un archivo `test_crm.py` con pruebas unitarias usando `pytest` para validar la lógica de negocio (cálculos `datetime`, validaciones).

## 🏃‍♂️ Cómo Empezar

1.  **Clonar el repositorio** (o descargar los archivos).
2.  **Estructura de archivos:** Asegurarse de que los CSV iniciales están en una carpeta `data/` al mismo nivel que `crm.py`:
    ```
    proyecto/
    │
    ├── crm.py
    ├── test_crm.py
    │
    └── data/
        ├── clientes.csv
        ├── eventos.csv
        └── ventas.csv
    ```
3.  **(Opcional) Instalar pytest:**
    ```bash
    pip install pytest
    ```
4.  **Ejecutar la aplicación:**
    ```bash
    python crm.py
    ```

## 🧪 Cómo Ejecutar las Pruebas

Para verificar que toda la lógica (cálculos de fechas, validaciones, etc.) funciona correctamente, ejecuta `pytest` en la terminal desde la carpeta raíz del proyecto:

```bash
pytest