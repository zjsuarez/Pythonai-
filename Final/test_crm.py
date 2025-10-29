import pytest
from datetime import date, timedelta
from crm import *

# Creamos datos de prueba para que los tests sean independientes de los CSV
# Usaremos una fecha de registro que pasó hace 10 días exactos para el test.
FECHA_PRUEBA_PASADA = (date.today() - timedelta(days=10)).strftime('%Y-%m-%d')
# Usaremos una fecha de evento que ocurrirá en 5 días exactos para el test.
FECHA_PRUEBA_FUTURA = (date.today() + timedelta(days=5)).strftime('%Y-%m-%d')


## --- PRUEBAS DE CLASES Y DATETIME ---

def test_cliente_antiguedad_dias():
    """Verifica que el cálculo de antiguedad_dias() es correcto."""
    
    # GIVEN: Un cliente registrado hace 10 días
    cliente_test = Cliente("c999", "Test", "test@mail.com", FECHA_PRUEBA_PASADA)
    
    # WHEN: Calculamos la antigüedad
    antiguedad = cliente_test.antiguedad_dias()
    
    # THEN: La antigüedad debe ser 10 días
    assert antiguedad == 10
    
def test_evento_dias_hasta_evento():
    """Verifica que el cálculo de dias_hasta_evento() es correcto."""
    
    # GIVEN: Un evento programado dentro de 5 días
    evento_test = Evento("e999", "Test", FECHA_PRUEBA_FUTURA, "10.00", "TestCat")
    
    # WHEN: Calculamos los días restantes
    dias_faltantes = evento_test.dias_hasta_evento()
    
    # THEN: Deben faltar 5 días
    assert dias_faltantes == 5

def test_evento_precio_conversion():
    """Verifica que el precio se convierte correctamente a float."""
    
    # GIVEN: Un precio en formato string
    evento_test = Evento("e999", "Test", FECHA_PRUEBA_FUTURA, "49.99", "TestCat")
    
    # THEN: El atributo precio debe ser un float con el valor correcto
    assert isinstance(evento_test.precio, float)
    assert evento_test.precio == 49.99


## --- PRUEBAS DE VALIDACIONES Y LÓGICA AUXILIAR ---

def test_generar_nuevo_id_cliente_inicio():
    """Verifica que el ID se genera correctamente si el diccionario está vacío."""
    # GIVEN: Un diccionario de clientes vacío
    clientes_vacio = {}
    
    # THEN: El primer ID debe ser 'c001'
    assert generar_nuevo_id_cliente(clientes_vacio) == "c001"

def test_generar_nuevo_id_cliente_incremental():
    """Verifica que el ID se genera correctamente basado en el conteo."""
    # GIVEN: Un diccionario con 3 clientes (c001, c002, c003)
    clientes_con_datos = {'c001': 'a', 'c002': 'b', 'c003': 'c'}
    
    # THEN: El siguiente ID debe ser 'c004'
    assert generar_nuevo_id_cliente(clientes_con_datos) == "c004"

def test_validar_email_correcto():
    """Verifica que un email válido pase la validación simple."""
    assert validar_email("usuario@dominio.es") is True
    
def test_validar_email_incorrecto():
    """Verifica que un email sin '@' o '.' falle la validación."""
    assert validar_email("usuariodominio.es") is False # Falta @
    assert validar_email("usuario@dominioes") is False # Falta .