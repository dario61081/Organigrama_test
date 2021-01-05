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
    raiz = Area(1, "Gerencia", 3)
    raiz.agregar_area_hija(Area(6, "Contabilidad", 10))
    factu = raiz.agregar_area_hija(Area(8, "Facturacion", 4))
    raiz.agregar_area_hija(Area(4, "Tesoreria", 6))

    factu.agregar_area_hija(Area(9, "Informatica", 4))
    factu.agregar_area_hija(Area(2, "Clientes", 3))

    z = Organigrama("Ejemplo 1", raiz)
    z.imprimir_organigrama()



    # print sumorg(z, 8)
    # print sumorg(z, 1)
    # print sumorg(z, 4)
