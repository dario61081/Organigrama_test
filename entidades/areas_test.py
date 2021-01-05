import unittest

from entidades import Area


class TestAreas(unittest.TestCase):
    """
    Verificar objeto Area
    """

    def setUp(self):
        self.area = Area(1, "GERENCIA", 10) # Mayusculas a proposito

    def test_instance(self):
        """
        Verificar si la instancia ha sido creada
        """
        self.assertIsNotNone(self.area, msg="Objeto no ha sido instanciado")

    def test_valor_codigo(self):
        """
        Verificar que este asignando el codigo
        """
        self.assertEqual(self.area.codigo, 1, msg="Codigo de nodo no coincide")

    def test_valor_nombre(self):
        """
        Verificar que este capitalizado el nombre del area
        """
        self.assertEqual(self.area.nombre, "Gerencia", msg="Nombre del area no coincide")

    def test_agregar_area_hija(self):
        self.area.agregar_area_hija(Area(2, "facturacion", 2))
        self.assertGreater(len(self.area.areas_hijas), 0, msg="No registra areas hijas en la instancia")

    def test_buscador_codigo(self):
        objeto = self.area.get(2)
        self.assertIsNotNone(objeto, msg="Area buscado no fue encontrado")
