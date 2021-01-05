__version__ = "1.0"
__author__ = "Dario Garcia"
__all__ = ['Organigrama']

from . import Area


class Organigrama:
    """
    Clase para manejo de un organigrama
    """

    def __init__(self, nombre):
        """
        Constructor organigrama
        :param nombre: nombre del organigrama
        """
        self.nombre = nombre
        self.nodos = []

    def imprimir(self):
        """
        Imprimir organigrama actual
        :return: None
        """

        print "Organigrama: \"{nombre}\"".format(nombre=self.nombre)
        for n in self.nodos:
            print(n)
        print "*** FIN ***"

    def add_nodo(self, nodo):
        """
        Agregar un nodo al organigrama
        :param nodo:
        :return: None
        """
        if isinstance(nodo, (Area,)):
            self.nodos.append(nodo)
        else:
            raise Exception("Tipo de nodo invalido")
