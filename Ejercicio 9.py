# Registro de eventos en un archivo log
from datetime import datetime

# Solicita el mensaje del usuario
mensaje = input("Escribe el mensaje del evento: ")

# Obtiene la fecha y hora actual
fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Crea la línea que se va a escribir
linea_log = f"[{fecha_hora}] {mensaje}\n"

# Abre el archivo log.txt y agrega la línea
with open("log.txt", "a", encoding="utf-8") as archivo_log:
    archivo_log.write(linea_log)

print("Evento registrado en log.txt.")
