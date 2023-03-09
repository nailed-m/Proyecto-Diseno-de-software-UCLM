#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Puerta(ElementoMapa):
    def __init__(self):
        self.abierta = False
        self.lado1 = None
        self.lado2 = None

    @property
    def abierta(self):
        return self.abierta

    @abierta.setter
    def abierta(self,_abierta):
        self.abierta=_abierta

    def entrar():
        if(abierta):
            print("Puedes pasar al otro lado")
        else:
            print("La puerta esta cerrada")
    
    def esPuerta():
        return True

    def estaCerrada(self):
        return self.abierta(self)

    @property
    def lado1(self):
        return self.lado1

    @lado1.setter
    def lado1(self,_lado1):
        self.lado1=_lado1

    @property
    def lado2(self):
        return self.lado2

    @lado2.setter
    def lado2(self,_lado2):
        self.lado2=_lado2

