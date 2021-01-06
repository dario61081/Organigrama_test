__version__ = "1.0"
__author__ = "Dario Garcia"

from entidades import *
from funciones.organigrama_funciones import leer_y_cargar_organigrama, sumorg

if __name__ == '__main__':
    # ejecutar rutinas de carga y acciones
    titulo = raw_input("Titulo del organigrama > ")
    if not titulo:
        titulo = "Empresa ABC"

    organigrama = leer_y_cargar_organigrama(Organigrama(titulo))

    if organigrama:
        cursor = "{} > "
        lectura = True
        while lectura:
            organigrama.imprimir_organigrama()
            try:
                codigo_area = int(raw_input(cursor.format("Codigo del area a ejecutar sumorg(?)| 0: Salir ")))
                if codigo_area:
                    if codigo_area == -1:
                        lectura = False
                    else:
                        valor = sumorg(organigrama, codigo_area)
                        print "{}".format(valor)
            except Exception as e:
                print "(!) {}".format(e)
