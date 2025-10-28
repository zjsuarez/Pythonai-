numerotrabajadores = int(input("Ingrese el número de trabajadores: "))


horareferencia = int(input("Ingrese la hora de referencia (0-23): "))



salidamastemprana = 24
nombresalidamastemprana = ""
numeroempleadoshorareferencia = 0

for i in range(numerotrabajadores):
    nombreempleado = input("nombre del empleado:")
    while (True):
            horaentrada = int(input("Hora entrada:"))
            if (horaentrada >=0 and horaentrada<=23):
                break
            else:
                continue
    
    while (True):
        while (True):
            horasalida = int(input("Hora salida:"))
            if (horasalida >=0 and horasalida<=23):
                break
            else:
                continue
        if (horasalida > horaentrada):
            break
        else:
            continue

    if horasalida < salidamastemprana:
        salidamastemprana = horasalida
        nombresalidamastemprana = nombreempleado
    
    if horaentrada <= horareferencia:
        numeroempleadoshorareferencia+=1


print("Empleado con salida mas temprana: " + str(nombresalidamastemprana))
print("Numeros empelados que han entrado antes o a la hora de referencia:" + str(numeroempleadoshorareferencia))

    