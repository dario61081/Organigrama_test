__version__ = "1.0"
__author__ = "Dario Garcia"

import unittest

from entidades import Organigrama


class TestOrganigrama(unittest.TestCase):
    """
    Verificar objeto Organigrama
    """

    def setUp(self):
        self.org = Organigrama("EMPRESA ABC")

    def test_instance(self):
        """
        verificar la instancia
        """
        self.assertIsNotNone(self.org, msg="Instancia no ha sido creada")

    def test_param_titulo_instance(self):
        # verificar si el titulo carga correctamente
        self.assertIsNotNone(self.org.titulo, msg="Nombre del organigrama no instanciado")

    def test_param_titulo_value(self):
        self.assertEqual(self.org.titulo, "EMPRESA ABC", msg="Valor del nombre no coincide")
