__version__ = "1.0"
__author__ = "Dario Garcia"
__all__ = ["Area"]


class Area:
    """
    Clase nodo para el organigrama
    """

    def __init__(self, codigo, codigo_padre, nombre, cantidad_funcionarios):
        """
        Nodo del organigrama, actua como area dentro de la organizacion
        :param codigo: codigo del area
        :param codigo_padre: codigo del area padre
        :param nombre: nombre del area
        :param cantidad_funcionarios: cantidad de funcionarios
        """
        self.codigo = codigo
        self.codigo_padre = codigo_padre
        self.nombre = nombre
        self.cantidad_funcionarios = cantidad_funcionarios
        self.nodos_hijos = []

    def __str__(self):
        return "{codigo}, {nombre}, {cantidad}".format(codigo=self.codigo,
                                                       nombre=self.nombre,
                                                       cantidad=self.cantidad_funcionarios)
