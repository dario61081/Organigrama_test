import unittest

from entidades import Area


class TestAreas(unittest.TestCase):
    """
    Verificar objeto Area
    """

    def setUp(self):
        self.area = Area(1, 0, "GERENCIA", 10)

    def test_instance(self):
        self.assertIsNotNone(self.area, msg="Objeto no ha sido instanciado")

    def test_valor_codigo(self):
        self.assertEqual(self.area.codigo, 1, msg="Codigo de nodo no coincide")

    def test_valor_codigo_padre(self):
        self.assertEqual(self.area.codigo_padre, 0, msg="Codigo del nodo padre no coincide")

    def test_valor_nombre(self):
        self.assertEqual(self.area.nombre, "GERENCIA", msg="Nombre del area no coincide")
