from datetime import datetime, date

# ---------------------------------------------
# CLASE EVENTO
# ---------------------------------------------

class Evento:
    def __init__(self, id_evento: str, nombre: str, fecha: str, precio: str, categoria: str):
        self.id_evento = id_evento
        self.nombre = nombre
        self.fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        self.precio = float(precio)
        self.categoria = categoria

    def __str__(self) -> str:
        return f"[{self.id_evento}] {self.nombre} ({self.categoria}) - Fecha: {self.fecha} - {self.precio:.2f}€"

    def dias_hasta_evento(self) -> int:
        hoy = date.today()
        diferencia = self.fecha - hoy
        return diferencia.days

