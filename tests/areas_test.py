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
        # agregar nodos hijas y buscar el segundo
        self.area.agregar_area_hija(Area(2, "test a", 10))
        self.area.agregar_area_hija(Area(3, "test b", 5))
        self.area.agregar_area_hija(Area(4, "test c", 2))

        objeto_a = self.area.get(2)  # cargado previamente
        self.assertIsNotNone(objeto_a, msg="Area 2 buscado no fue encontrado")
        self.assertEqual(objeto_a.codigo, 2, msg="Codigo del area no es igual")

        objeto_b = self.area.get(4)
        self.assertIsNotNone(objeto_b, msg="Area 4 buscada no fue encontrada")
        self.assertEqual(objeto_b.codigo, 4, msg="Codigo del area no es igual")

    def test_cantidad_funcionarios(self):
        cantidad = self.area.get_cantidades_funcionarios()
        self.assertEqual(10, cantidad, msg="Cantidad de funcionario no coincide")

        # agregar nodo y reconteo

        self.area.agregar_area_hija(Area(2, "test a", 2))
        # self.area.agregar_area_hija(Area(3, "test b", 5))

        cantidad = self.area.get_cantidades_funcionarios()
        self.assertEqual(25, cantidad, msg="Cantidad de funcionarios no coincide")
