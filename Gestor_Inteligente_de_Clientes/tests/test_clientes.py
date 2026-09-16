import unittest
from clientes import ClienteRegular, ClientePremium, ClienteCorporativo
from validaciones import validar_email, EmailInvalidoError


class TestClientes(unittest.TestCase):
    def test_cliente_regular(self):
        cliente = ClienteRegular("Ana", "ana@mail.com", "912345678", "Calle 1")
        self.assertEqual(cliente.tipo_cliente(), "Regular")

    def test_herencia_y_polimorfismo(self):
        clientes = [
            ClienteRegular("Ana", "a@mail.com", "912345678", "Calle 1"),
            ClientePremium("Luis", "l@mail.com", "912345679", "Calle 2"),
            ClienteCorporativo("Pedro", "p@mail.com", "912345670", "Calle 3", "Empresa SpA")
        ]
        tipos = [cliente.tipo_cliente() for cliente in clientes]
        self.assertEqual(tipos, ["Regular", "Premium", "Corporativo"])

    def test_email_invalido(self):
        with self.assertRaises(EmailInvalidoError):
            validar_email("correo_incorrecto")

    def test_metodo_str(self):
        cliente = ClienteRegular("Ana", "ana@mail.com", "912345678", "Calle 1")
        self.assertIn("Ana", str(cliente))


if __name__ == "__main__":
    unittest.main()
