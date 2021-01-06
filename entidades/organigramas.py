__version__ = "1.0"
__author__ = "Dario Garcia"
__all__ = ['Organigrama']

import json
import os


class Organigrama:
    """
    Clase para manejo de un organigrama
    """

    def __init__(self, titulo):
        """
        Constructor organigrama
        :param nombre: nombre del organigrama
        """
        self.titulo = titulo
        self.raiz = None

    def imprimir_organigrama(self):
        print "\n\n*** Organigrama \"{titulo}\" ***".format(titulo=self.titulo)
        if self.raiz:
            self.raiz.imprimir_jerarquia()
        else:
            print "El organigrama no tiene areas definidas"
        print "\n\n"

    def get_area(self, codigo_area):
        """
        Obtener el area por medio del codigo de area
        :param codigo_area: codigo (int)
        :return: objeto area relacionado
        """
        if self.raiz:
            return self.raiz.get(codigo_area)

    def sumorg(self, codigo_area):
        """
        Devuelve la sumatoria de funcionarios del area y areas relacionadas
        :param codigo_area: codigo del area
        :return: sumatoria de funcionarios (int)
        """
        inicio = self.get_area(codigo_area)
        if inicio:
            return inicio.sumorg()
        else:
            print "Area con el codigo {codigo_area} no existe".format(codigo_area=codigo_area)
            return 0
