__version__ = "1.0"
__author__ = "Dario Garcia"

from entidades import *


def sumorg(organigrama, codigo_nodo):
    """
    Funcion para hacer conteo de cantidad de funcionarios por nodos de una jerarquia
    :return:
    """
    if not isinstance(organigrama, (Organigrama,)):
        raise Exception("El organigrama a procesar no es un objeto valido")
    if not isinstance(codigo_nodo, (int,)):
        raise Exception("Codigo de nodo no es numerico")

    return 11


if __name__ == '__main__':

    z = Organigrama("Ejemplo 1")

    z.add_nodo(Area(1, 0, "Gerencia", 3))
    z.add_nodo(Area(6, 1, "Facturacion", 4))
    z.add_nodo(Area(4, 1, "Contabilidad", 10))
    z.add_nodo(Area(8, 1, "Tesoreria", 6))
    z.add_nodo(Area(9, 8, "Informatica", 4))
    z.add_nodo(Area(2, 8, "Clientes", 3))

    print sumorg(z, 8)
    print sumorg(z, 1)
    print sumorg(z, 4)
