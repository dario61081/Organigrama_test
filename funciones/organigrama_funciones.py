__version__ = "1.0"
__author__ = "Dario Garcia"

from entidades import Organigrama, Area


def leer_y_cargar_organigrama(organigrama):
    # print "Lectura de organigrama \"{titulo}\"".format(titulo=organigrama.titulo)
    lectura = True
    cursor = "{} > "
    while lectura:
        # vista previa
        organigrama.imprimir_organigrama()
        # seleccione accion?
        comando = raw_input(cursor.format("Accion: (a: nuevo | b: borrar | i: imprimir | x: salir "))
        if comando in ('a', 'b', 'i', 'x'):
            if comando == 'a':
                # agregar nodo
                codigo = int(raw_input(cursor.format("Codigo del area")))
                nombre = raw_input(cursor.format("Nombre del area"))
                cantidad = int(raw_input(cursor.format("Cantidad del area")))
                nueva_area = Area(codigo, nombre, cantidad)

                if organigrama.raiz:
                    codigo_padre = int(raw_input(cursor.format("Codigo del area padre a asignar")))
                    area = organigrama.raiz.get(codigo_padre)
                    if area:
                        area.agregar_area_hija(nueva_area)
                    print "Agregado al area {}".format(codigo_padre)
                else:
                    organigrama.raiz = nueva_area
                    print "Agregado area como raiz del organigrama"

            elif comando == 'b':
                # quitar nodo
                codigo = int(raw_input(cursor.format("Codigo del area a borrar")))
                if organigrama.raiz:
                    organigrama.raiz.borrar_area(codigo)
                else:
                    print "Organigrama sin areas definidas"

            # elif comando == 'i':
            #     # imprimir organigrama
            #     if organigrama.raiz:
            #         organigrama.raiz.imprimir_jerarquia()
            #     else:
            #         print "Organigrama sin areas definidas"

            # elif comando == 's':
            #     # sumorg
            #     codigo_padre = int(raw_input(cursor.format("ingrese codigo de area a ejecutar sumorg(?)")))
            #     if codigo_padre:
            #         valor = organigrama.raiz.sumorg(codigo_padre)
            #         print "sumorg({}) = {}".format(codigo_padre, valor)

            elif comando == 'x':
                # terminar loop
                lectura = False
                print "** Fin **"

        else:
            print "Comando invalido"

    return organigrama


def sumorg(organigrama, codigo_nodo):
    """
    Funcion para hacer conteo de cantidad de funcionarios por nodos de una jerarquia
    :return:
    """
    if not isinstance(organigrama, (Organigrama,)):
        raise Exception("El argumento pasado como organigrama no es valido")

    if not isinstance(codigo_nodo, (int,)):
        raise Exception("Codigo de nodo no es numerico")

    r = organigrama.get_area(codigo_nodo)
    if not isinstance(r, (Area,)):
        return 0
    else:
        return r.get_cantidades_funcionarios()
