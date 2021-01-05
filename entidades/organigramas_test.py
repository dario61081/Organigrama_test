__version__ = "1.0"
__author__ = "Dario Garcia"

import unittest

from entidades import Organigrama, Area


class TestOrganigrama(unittest.TestCase):
    """
    Verificar objeto Organigrama
    """

    def setUp(self):
        self.org = Organigrama("EMPRESA ABC")

    def test_instance(self):
        self.assertIsNotNone(self.org, msg="Instancia no ha sido creada")

    def test_param_nombre(self):
        self.assertIsNotNone(self.org.nombre, msg="Nombre del organigrama no instanciado")

    def test_param_nombre_value(self):
        self.assertEqual(self.org.nombre, "EMPRESA ABC", msg="Valor del nombre no coincide")

    def test_nodos(self):
        self.assertIsNotNone(self.org.nodos, msg="Nodos no han sido instanciados")

    def test_add_nodo(self):
        self.org.add_nodo(Area(1, 1, "test", 1))
        self.assertGreater(len(self.org.nodos), 0, msg="No se puede registrar nodo hijo")
