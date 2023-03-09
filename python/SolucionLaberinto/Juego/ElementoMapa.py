#!/usr/bin/python
#-*- coding: utf-8 -*-

import abc

class ElementoMapa:
    def __init__(self):
        self.padre = None

    @abc.abstractmethod
    def entrar(self, input):
        """No es lo mismo entrar en una habitacion, que en una pared, que en una puerta.
        Asi que vamos a delegar.
        No es buena idea dejar que el metodo de la superclase por defecto se quede en blanco, porque si algo fallara no podriamos enterarnos.
        Una mejor idea es obligar a las subclases a implementar este metodo.
        """
        return

    @abc.abstractmethod
    def entrar(alguien):
        """No es lo mismo entrar en una habitacion, que en una pared, que en una puerta.
        Asi que vamos a delegar.
        No es buena idea dejar que el metodo de la superclase por defecto se quede en blanco, porque si algo fallara no podriamos enterarnos.
        Una mejor idea es obligar a las subclases a implementar este metodo.
        """
        return

    def esBomba():
        return False

    def esHabitacion():
        return False

    def esPared():
        return False

    def esPuerta():
        return False

    @property
    def padre(self):
        return self.padre
    
    @padre.setter
    def padre(self,_padre):
        self.padre=_padre

    def recorrer(unBloque):
        unBloque.value(self)
