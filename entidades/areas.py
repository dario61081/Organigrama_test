__version__ = "1.0"
__author__ = "Dario Garcia"
__all__ = ["Area"]


class Area:

    def __init__(self, codigo, nombre, cantidad):
        """
        Nodo del organigrama, actua como area dentro de la organizacion
        :param codigo: codigo del area
        :param nombre: nombre del area
        :param cantidad: cantidad de funcionarios
        """
        self.codigo = codigo
        self.nombre = str(nombre).capitalize()
        self.cantidad = cantidad
        self.areas_hijas = []
        self.padre = None

    def agregar_area_hija(self, nueva_area_hija):
        """
        Registrar un area hija
        :param nueva_area_hija: objeto area
        :return:
        """
        if not isinstance(nueva_area_hija, (Area,)):
            raise Exception("Nodo a insertar no es valido")
        nueva_area_hija.padre = self
        self.areas_hijas.append(nueva_area_hija)
        return nueva_area_hija

    def jerarquia(self):
        salto = 0
        padre = self.padre
        while padre:
            salto += 1
            padre = padre.padre

        return salto

    def imprimir(self):
        print(self)
        if self.areas_hijas:
            for i in self.areas_hijas:
                i.imprimir()

    def __str__(self):
        marca = " " * self.jerarquia() * (2) + "+" if self.padre else "+"
        return "{marca} {nombre} ({cantidad})".format(marca=marca,
                                                      nombre=self.nombre,
                                                      cantidad=self.cantidad
                                                      )
