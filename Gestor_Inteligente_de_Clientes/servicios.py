import json
from datetime import datetime
from urllib.request import urlopen


def registrar_actividad(mensaje):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("actividad.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{fecha} - {mensaje}\n")


def probar_api():
    try:
        respuesta = urlopen(
            "https://jsonplaceholder.typicode.com/users/1",
            timeout=5
        )
        datos = json.loads(respuesta.read().decode("utf-8"))
        if datos.get("id"):
            return "Conexión con API realizada correctamente"
    except Exception:
        return "No se pudo conectar con la API"
    return "Respuesta de API no válida"


def notificacion_bienvenida(nombre, email):
    mensaje = f"Bienvenida registrada para {nombre} - {email}"
    registrar_actividad(mensaje)
    return mensaje
