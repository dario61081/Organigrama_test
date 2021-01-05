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

    def cargar_archivo(self, filename):
        """
        Cargar el organigrama desde un archivo
        :param filename: ruta del archivo *.json

        """
        if not filename:
            raise Exception("Argumento de archivo no definido")

        if not os.path.exists(filename):
            raise Exception("Archivo no existente")

        print("Leyendo archivo {filename}".format(filename=filename))

        with open(filename, "r") as f:
            datos = json.loads(f.read())

        # identificar titulo
        self.titulo = datos['titulo'] or "sin titulo"
        areas = datos['areas']

        def leer_nodo_siguiente(nodo):
            return

        for item in areas:
            pass

        if len(areas) == 0:
            raise Exception("(!) Este organigrama no tiene areas definidas")
        else:
            print "Leyendo areas del organigrama..."

        print "Organigrama \"{titulo}\" listo".format(titulo=self.titulo)

    def imprimir_organigrama(self):
        print "\n\n*** Organigrama \"{titulo}\" ***".format(titulo=self.titulo)
        if self.raiz:
            self.raiz.imprimir_jerarquia()
        else:
            print "El organigrama no tiene areas definidas"

    def get_area(self, codigo_area):
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
            return inicio.get_cantidades_funcionarios()
        else:
            print "Area con el codigo {codigo_area} no existe".format(codigo_area=codigo_area)
            return 0
