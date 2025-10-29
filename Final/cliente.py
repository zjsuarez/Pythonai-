from datetime import datetime, date

# ---------------------------------------------
# CLASE CLIENTE
# ---------------------------------------------
class Cliente:
    def __init__(self, id_cliente: str, nombre: str, email: str, fecha_registro: str):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.fecha_registro = datetime.strptime(fecha_registro, '%Y-%m-%d').date()

    def __str__(self) -> str:
        return f"[{self.id_cliente}] {self.nombre} ({self.email}) - Miembro desde: {self.fecha_registro}"

    def antiguedad_dias(self) -> int:
        hoy = date.today()
        diferencia = hoy - self.fecha_registro
        return diferencia.days