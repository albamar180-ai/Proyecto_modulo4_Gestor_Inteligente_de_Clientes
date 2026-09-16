import tkinter as tk
from tkinter import messagebox, ttk

from clientes import ClienteRegular, ClientePremium, ClienteCorporativo
from validaciones import validar_email, validar_telefono
from servicios import probar_api, notificacion_bienvenida


class AplicacionClientes(tk.Tk):
    def __init__(self, gestor):
        super().__init__()
        self.gestor = gestor
        self.title("Gestor Inteligente de Clientes")
        self.geometry("900x600")
        self.crear_formulario()
        self.crear_tabla()
        self.mostrar_clientes()

    def crear_formulario(self):
        tk.Label(self, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
        self.nombre = tk.Entry(self, width=30)
        self.nombre.grid(row=0, column=1)

        tk.Label(self, text="Email").grid(row=1, column=0, padx=5, pady=5)
        self.email = tk.Entry(self, width=30)
        self.email.grid(row=1, column=1)

        tk.Label(self, text="Teléfono").grid(row=2, column=0, padx=5, pady=5)
        self.telefono = tk.Entry(self, width=30)
        self.telefono.grid(row=2, column=1)

        tk.Label(self, text="Dirección").grid(row=3, column=0, padx=5, pady=5)
        self.direccion = tk.Entry(self, width=30)
        self.direccion.grid(row=3, column=1)

        tk.Label(self, text="Tipo").grid(row=0, column=2, padx=5)
        self.tipo = ttk.Combobox(self, values=["Regular", "Premium", "Corporativo"], state="readonly")
        self.tipo.current(0)
        self.tipo.grid(row=0, column=3)

        tk.Label(self, text="Dato extra").grid(row=1, column=2, padx=5)
        self.extra = tk.Entry(self, width=25)
        self.extra.grid(row=1, column=3)

        tk.Label(self, text="Buscar").grid(row=4, column=0, padx=5, pady=5)
        self.buscar = tk.Entry(self, width=30)
        self.buscar.grid(row=4, column=1)

        tk.Button(self, text="Agregar", command=self.agregar).grid(row=5, column=0, pady=10)
        tk.Button(self, text="Editar", command=self.editar).grid(row=5, column=1)
        tk.Button(self, text="Eliminar", command=self.eliminar).grid(row=5, column=2)
        tk.Button(self, text="Buscar", command=self.buscar_datos).grid(row=5, column=3)
        tk.Button(self, text="Mostrar todos", command=self.mostrar_clientes).grid(row=6, column=0)
        tk.Button(self, text="Exportar JSON", command=self.exportar_json).grid(row=6, column=1)
        tk.Button(self, text="Exportar CSV", command=self.exportar_csv).grid(row=6, column=2)
        tk.Button(self, text="Probar API", command=self.ver_api).grid(row=6, column=3)

    def crear_tabla(self):
        columnas = ("id", "nombre", "email", "telefono", "direccion", "tipo")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=16)
        for columna in columnas:
            self.tabla.heading(columna, text=columna.capitalize())
        self.tabla.grid(row=7, column=0, columnspan=4, padx=10, pady=15)

    def crear_objeto_cliente(self):
        nombre = self.nombre.get().strip()
        email = self.email.get().strip()
        telefono = self.telefono.get().strip()
        direccion = self.direccion.get().strip()
        tipo = self.tipo.get()
        extra = self.extra.get().strip()

        if nombre == "" or direccion == "":
            raise ValueError("Nombre y dirección son obligatorios")
        validar_email(email)
        validar_telefono(telefono)

        if tipo == "Premium":
            descuento = 10 if extra == "" else int(extra)
            return ClientePremium(nombre, email, telefono, direccion, descuento)
        if tipo == "Corporativo":
            if extra == "":
                raise ValueError("Debe ingresar la empresa del cliente corporativo")
            return ClienteCorporativo(nombre, email, telefono, direccion, extra)

        puntos = 0 if extra == "" else int(extra)
        return ClienteRegular(nombre, email, telefono, direccion, puntos)

    def agregar(self):
        try:
            cliente = self.crear_objeto_cliente()
            self.gestor.crear_cliente(cliente)
            notificacion_bienvenida(cliente.get_nombre(), cliente.get_email())
            messagebox.showinfo("Información", "Cliente agregado")
            self.limpiar()
            self.mostrar_clientes()
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def editar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione un cliente")
            return
        try:
            datos = self.tabla.item(seleccion[0])["values"]
            nombre = self.nombre.get().strip()
            telefono = self.telefono.get().strip()
            direccion = self.direccion.get().strip()
            if nombre == "" or direccion == "":
                raise ValueError("Escriba nombre, teléfono y dirección para editar")
            validar_telefono(telefono)
            self.gestor.editar_cliente(datos[0], nombre, telefono, direccion)
            messagebox.showinfo("Información", "Cliente editado")
            self.mostrar_clientes()
        except Exception as error:
            messagebox.showerror("Error", str(error))

    def eliminar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione un cliente")
            return
        datos = self.tabla.item(seleccion[0])["values"]
        self.gestor.eliminar_cliente(datos[0])
        self.mostrar_clientes()

    def buscar_datos(self):
        texto = self.buscar.get().strip()
        clientes = self.gestor.buscar_cliente(texto) if texto else self.gestor.listar_clientes()
        self.cargar_tabla(clientes)

    def mostrar_clientes(self):
        self.cargar_tabla(self.gestor.listar_clientes())

    def cargar_tabla(self, clientes):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for cliente in clientes:
            self.tabla.insert("", tk.END, values=(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]))

    def exportar_json(self):
        self.gestor.exportar_json()
        messagebox.showinfo("Información", "Se creó data/clientes.json")

    def exportar_csv(self):
        self.gestor.exportar_csv()
        messagebox.showinfo("Información", "Se creó data/clientes.csv")

    def ver_api(self):
        messagebox.showinfo("API", probar_api())

    def limpiar(self):
        self.nombre.delete(0, tk.END)
        self.email.delete(0, tk.END)
        self.telefono.delete(0, tk.END)
        self.direccion.delete(0, tk.END)
        self.extra.delete(0, tk.END)
        self.tipo.current(0)
