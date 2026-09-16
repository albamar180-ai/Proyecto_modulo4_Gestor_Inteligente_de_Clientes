# Proyecto Módulo 4 - Gestor Inteligente de Clientes

**Estudiante:** Alba Moreno  
**Bootcamp:** Full Stack Python

Este proyecto corresponde a la evaluación del Módulo 4 y su objetivo es aplicar
los contenidos principales vistos como lo son: clases, objetos,
encapsulación, herencia, polimorfismo, diagramas de clase, manejo de errores,
excepciones y archivos.

También se incluyen algunos requerimientos indicados en la pauta del proyecto como:
SQLite, una interfaz sencilla con Tkinter, una conexión demostrativa con una API
pública, logs y pruebas unitarias.

## Archivos principales

- `main.py`: inicia el programa.
- `clientes.py`: contiene la clase Cliente y sus subclases.
- `validaciones.py`: contiene validaciones y excepciones.
- `database.py`: guarda, busca, edita y elimina clientes en SQLite.
- `gestorClientes.py`: organiza las operaciones principales del gestor.
- `archivos.py`: exporta información a JSON y CSV.
- `servicios.py`: registra actividad en `actividad.txt` y prueba una API pública.
- `gui.py`: contiene la interfaz gráfica.
- `docs/diagrama_uml.md`: diagrama de clases.
- `tests/test_clientes.py`: pruebas básicas.

## Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

## Cómo ejecutar las pruebas

```bash
python -m unittest discover tests
```

## Ejemplo de POO

```python
cliente = ClientePremium(
    "Ana Pérez",
    "ana@mail.com",
    "912345678",
    "Calle Principal 123"
)

print(cliente)
print(cliente.tipo_cliente())
print(cliente.beneficio())
```

No es necesario instalar librerías externas.
A.M
