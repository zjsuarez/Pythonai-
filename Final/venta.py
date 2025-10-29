from datetime import datetime, date

# ---------------------------------------------
# CLASE VENTA
# ---------------------------------------------

class Venta:
    def __init__(self, id_venta: str, id_cliente: str, id_evento: str, fecha_venta: str):
        self.id_venta = id_venta
        self.id_cliente = id_cliente
        self.id_evento = id_evento
        # [Requisito datetime]
        self.fecha_venta = datetime.strptime(fecha_venta, '%Y-%m-%d').date()

    def __str__(self) -> str:
        return f"[{self.id_venta}] Cliente: {self.id_cliente} -> Evento: {self.id_evento} (Fecha Venta: {self.fecha_venta})"
    
    
    

     