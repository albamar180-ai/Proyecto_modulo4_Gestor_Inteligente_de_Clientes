class EmailInvalidoError(Exception):
    pass


class TelefonoInvalidoError(Exception):
    pass


def validar_email(email):
    if "@" not in email or "." not in email:
        raise EmailInvalidoError("El correo electrónico no es válido")


def validar_telefono(telefono):
    telefono_limpio = telefono.replace("+", "").replace(" ", "")

    if not telefono_limpio.isdigit():
        raise TelefonoInvalidoError("El teléfono debe contener números")

    if len(telefono_limpio) < 8:
        raise TelefonoInvalidoError("El teléfono debe tener al menos 8 dígitos")
