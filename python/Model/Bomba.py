#!/usr/bin/python
#-*- coding: utf-8 -*-

from Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        self.activa = False

    @property
    def activa(self):
        return self.activa

    @activa.setter
    def activa(self,_activa):
        self.activa=_activa

    def entrar(self):
        if self.activa==True:
            print("la bomba ha explotado")
            self.activa(self, False)
        else:
            self.component.entrar()

    def esBomba():
        return True