__version__ = "1.0"
__author__ = "Dario Garcia"
__all__ = ['Organigrama']

import json
import os

from . import Area


class Organigrama:
    """
    Clase para manejo de un organigrama
    """

    def __init__(self, filename):
        """
        Constructor organigrama
        :param nombre: nombre del organigrama
        """
        self.titulo = ""
        self.raiz = None

        if not filename:
            raise Exception("Argumento de archivo no definido")




    def imprimir_organigrama(self):
        print "*** Organigrama {titulo} ***".format(titulo=self.titulo)
        self.raiz.imprimir()

    def get_area(self, codigo_area):
        return self.raiz.get(codigo_area)








