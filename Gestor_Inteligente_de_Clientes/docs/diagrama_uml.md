# Diagrama de clases

```text
                         +----------------------+
                         |       Cliente        |
                         +----------------------+
                         | - nombre             |
                         | - email              |
                         | - telefono           |
                         | - direccion          |
                         +----------------------+
                         | + obtener_datos()    |
                         | + __str__()          |
                         | + __eq__()           |
                         +----------+-----------+
                                    |
                +-------------------+-------------------+
                |                   |                   |
        +-------v-------+   +-------v-------+   +-------v----------+
        |ClienteRegular|   |ClientePremium |   |ClienteCorporativo|
        +---------------+   +---------------+   +------------------+
        | - puntos      |   | - descuento   |   | - empresa        |
        +---------------+   +---------------+   +------------------+
```

Las tres subclases heredan de `Cliente`. Cada una tiene un dato propio y sobrescribe
`obtener_datos()`, lo que permite demostrar herencia y polimorfismo.
