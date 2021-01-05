import unittest

from entidades import Area


class TestAreas(unittest.TestCase):
    """
    Verificar objeto Area
    """

    def setUp(self):
        self.area = Area(1, "GERENCIA", 10)  # Mayusculas a proposito

    def test_instance(self):
        """
        Verificar si la instancia ha sido creada
        """
        self.assertIsNotNone(self.area, msg="Objeto no ha sido instanciado")

    def test_codigo(self):
        """
        Verificar que este asignando el codigo
        """
        self.assertIsNotNone(self.area.codigo, msg="Codigo no esta definido")
        self.assertEqual(self.area.codigo, 1, msg="Codigo de nodo no coincide")

    def test_nombre(self):
        """
        Verificar que este capitalizado el nombre del area
        """
        self.assertIsNotNone(self.area.nombre, msg="Nombre no esta definido")
        self.assertEqual(self.area.nombre, "Gerencia", msg="Nombre del area no coincide")

    def test_agregar_area_hija(self):
        # agregar un area hija
        nuevo_nodo = Area(2, "facturacion", 2)
        self.area.agregar_area_hija(nuevo_nodo)
        self.assertGreater(len(self.area.areas_hijas), 0, msg="No registra areas hijas en la instancia")
        self.assertEqual(len(self.area.areas_hijas), 1, msg="La cantidad de hijas es distinta a la esperada")

    def test_buscador_codigo(self):
        nuevo_nodo = Area(2, "facail"
                             "turacion", 3)
        objeto = self.area.get(2)
        self.assertIsNotNone(objeto, msg="Area buscado no fue encontrado")

        objeto = self.area.get(3)
        self.assertIsNotNone(objeto, msg="Area buscada no fue encontrada")

    def test_cantidad_funcionarios(self):
        cantidad = self.area.get_cantidades_funcionarios()
        self.assertEqual(cantidad, 10, msg="Cantidad de funcionario no coincide")
