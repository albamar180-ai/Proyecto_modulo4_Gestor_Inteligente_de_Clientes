import sqlite3
from clientes import ClienteCorporativo, ClientePremium, ClienteRegular


class BaseDatos:
    def __init__(self):
        self.nombre_bd = "data/clientes.db"

    def conectar(self):
        return sqlite3.connect(self.nombre_bd)

    def crear_tabla(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                email TEXT UNIQUE,
                telefono TEXT,
                direccion TEXT,
                tipo TEXT,
                empresa TEXT
            )
        """)
        conexion.commit()
        conexion.close()

    def agregar_cliente(self, cliente):
        conexion = self.conectar()
        cursor = conexion.cursor()

        dato_extra = ""
        if isinstance(cliente, ClienteCorporativo):
            dato_extra = cliente.get_empresa()
        elif isinstance(cliente, ClientePremium):
            dato_extra = str(cliente.get_descuento())
        elif isinstance(cliente, ClienteRegular):
            dato_extra = str(cliente.get_puntos())

        cursor.execute("""
            INSERT INTO clientes
            (nombre, email, telefono, direccion, tipo, empresa)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            cliente.get_nombre(), cliente.get_email(), cliente.get_telefono(),
            cliente.get_direccion(), cliente.tipo_cliente(), dato_extra
        ))
        conexion.commit()
        conexion.close()

    def listar_clientes(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes")
        datos = cursor.fetchall()
        conexion.close()
        return datos

    def buscar_cliente(self, texto):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT * FROM clientes
            WHERE nombre LIKE ? OR email LIKE ?
        """, (f"%{texto}%", f"%{texto}%"))
        datos = cursor.fetchall()
        conexion.close()
        return datos

    def editar_cliente(self, cliente_id, nombre, telefono, direccion):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE clientes
            SET nombre = ?, telefono = ?, direccion = ?
            WHERE id = ?
        """, (nombre, telefono, direccion, cliente_id))
        conexion.commit()
        conexion.close()

    def eliminar_cliente(self, cliente_id):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
        conexion.commit()
        conexion.close()
