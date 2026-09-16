from archivos import guardar_csv, guardar_json
from servicios import registrar_actividad


class GestorClientes:
    def __init__(self, base_datos):
        self.base_datos = base_datos

    def crear_cliente(self, cliente):
        self.base_datos.agregar_cliente(cliente)
        registrar_actividad(f"Cliente creado: {cliente.get_email()}")

    def listar_clientes(self):
        return self.base_datos.listar_clientes()

    def buscar_cliente(self, texto):
        return self.base_datos.buscar_cliente(texto)

    def editar_cliente(self, cliente_id, nombre, telefono, direccion):
        self.base_datos.editar_cliente(cliente_id, nombre, telefono, direccion)
        registrar_actividad(f"Cliente editado: ID {cliente_id}")

    def eliminar_cliente(self, cliente_id):
        self.base_datos.eliminar_cliente(cliente_id)
        registrar_actividad(f"Cliente eliminado: ID {cliente_id}")

    def exportar_json(self):
        guardar_json(self.listar_clientes())

    def exportar_csv(self):
        guardar_csv(self.listar_clientes())
