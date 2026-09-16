import json
import csv


def guardar_json(clientes):
    lista = []

    for cliente in clientes:
        lista.append({
            "id": cliente[0],
            "nombre": cliente[1],
            "email": cliente[2],
            "telefono": cliente[3],
            "direccion": cliente[4],
            "tipo": cliente[5],
            "empresa": cliente[6]
        })

    with open("data/clientes.json", "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)


def guardar_csv(clientes):
    with open("data/clientes.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([
            "ID", "Nombre", "Email", "Teléfono",
            "Dirección", "Tipo", "Empresa"
        ])

        for cliente in clientes:
            escritor.writerow(cliente)
