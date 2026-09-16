from database import BaseDatos
from gestorClientes import GestorClientes
from gui import AplicacionClientes


if __name__ == "__main__":
    base_datos = BaseDatos()
    base_datos.crear_tabla()
    gestor = GestorClientes(base_datos)
    app = AplicacionClientes(gestor)
    app.mainloop()
