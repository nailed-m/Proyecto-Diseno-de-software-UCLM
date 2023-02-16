#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Habitacion(ElementoMapa):
    def __init__(self,num):
        self.norte = None
        self.sur = None
        self.este = None
        self.oeste = None
        self.num=num

    def entrar(self):
        print("estas en la habitacion ", self.num)

    def esBomba():
        return False

    def esHabitacion():
        return True

    def esPared():
        return False

    def esPuerta():
        return False

    @property
    def este(self):
        return self.este

    @este.setter
    def este(self,_este):
        self.este=_este

    @property
    def norte(self):
        return self.norte

    @norte.setter
    def norte(self,_norte):
        self.norte=_norte

    @property
    def num(self):
        return self.num

    @num.setter
    def num(self,_num):
        self.num=_num

    @property
    def oeste(self):
        return self.oeste

    @oeste.setter
    def oeste(self,_oeste):
        self.oeste=_oeste

    @property
    def sur(self):
        return self.sur

    @oeste.setter
    def sur(self,_sur):
        self.sur=_sur

