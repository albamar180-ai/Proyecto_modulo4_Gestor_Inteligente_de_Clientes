class Cliente:
    def __init__(self, nombre, email, telefono, direccion):
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono
        self.__direccion = direccion

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_telefono(self):
        return self.__telefono

    def get_direccion(self):
        return self.__direccion

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def tipo_cliente(self):
        return "Cliente"

    def beneficio(self):
        return "Sin beneficio especial"

    def obtener_datos(self):
        return f"{self.__nombre} - {self.__email}"

    def __str__(self):
        return self.obtener_datos()

    def __eq__(self, otro):
        if isinstance(otro, Cliente):
            return self.__email == otro.get_email()
        return False


class ClienteRegular(Cliente):
    def __init__(self, nombre, email, telefono, direccion, puntos=0):
        super().__init__(nombre, email, telefono, direccion)
        self.__puntos = puntos

    def get_puntos(self):
        return self.__puntos

    def tipo_cliente(self):
        return "Regular"

    def beneficio(self):
        return "Atención normal"

    def obtener_datos(self):
        return f"{super().obtener_datos()} - Regular - Puntos: {self.__puntos}"


class ClientePremium(Cliente):
    def __init__(self, nombre, email, telefono, direccion, descuento=10):
        super().__init__(nombre, email, telefono, direccion)
        self.__descuento = descuento

    def get_descuento(self):
        return self.__descuento

    def tipo_cliente(self):
        return "Premium"

    def beneficio(self):
        return f"{self.__descuento}% de descuento"

    def obtener_datos(self):
        return f"{super().obtener_datos()} - Premium - Descuento: {self.__descuento}%"


class ClienteCorporativo(Cliente):
    def __init__(self, nombre, email, telefono, direccion, empresa):
        super().__init__(nombre, email, telefono, direccion)
        self.__empresa = empresa

    def get_empresa(self):
        return self.__empresa

    def tipo_cliente(self):
        return "Corporativo"

    def beneficio(self):
        return "Atención prioritaria"

    def obtener_datos(self):
        return f"{super().obtener_datos()} - Corporativo - Empresa: {self.__empresa}"
