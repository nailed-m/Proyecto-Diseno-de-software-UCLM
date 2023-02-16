#!/usr/bin/python
#-*- coding: utf-8 -*-

class Bicho():
    def __init__(self):
        self.modo=None
        self.poder=None
        self.posicion=None
        self.vidas=None
    
    @property
    def modo(self):
        return self.modo

    @modo.setter
    def modo(self, _modo):
        self.modo=_modo
    
    @property
    def poder(self):
        return self.poder
    
    @poder.setter
    def poder(self, _poder):
        self.poder=_poder

    @property
    def posicion(self):
        return self.posicion
    
    @posicion.setter
    def posicion(self, _posicion):
        self.posicion=_posicion
    
    @property
    def vidas(self):
        return self.vidas
    
    @vidas.setter
    def vidas(self, _vidas):
        self.vidas=_vidas
    