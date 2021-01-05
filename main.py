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
    z = Organigrama("Ejemplo 1", Area(1, "GERENCIA", 0))
    z.imprimir_organigrama()

    gerencia = z.get_area(0)


    # print sumorg(z, 8)
    # print sumorg(z, 1)
    # print sumorg(z, 4)
