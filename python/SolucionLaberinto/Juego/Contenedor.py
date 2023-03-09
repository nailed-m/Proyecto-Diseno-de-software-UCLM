#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
import math

from ElementoMapa import ElementoMapa

class Contenedor(ElementoMapa):
    def __init__(self):
        self.hijos={}
        self.este=None
        self.norte=None
        self.num=None
        self.oeste=None
        self.sur=None
        self.orientaciones={}

    def agregarOrientacion(unaOr):
        self.orientaciones(self).add(unaOr)
    
    @property
    def este(self):
        return self.este

    @este.setter
    def este(self,_este):
        self.este=_este

    @property
    def hijos(self):
        return self.hijos

    @hijos.setter
    def hijos(self,_hijos):
        self.hijos=_hijos

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

    def obtenerNumeroAleatorio(numMax):
        rand=random.random()
        resultado = math.trunc(1 + (rand*numMax))
        return resultado

    def obtenerOrientacionAleatoria():
        ind=self.obtenerNumeroAleatorio(len(self.orientaciones(self)))
        return self.orientaciones(self).values()[ind]

    @property
    def oeste(self):
        return self.oeste

    @oeste.setter
    def oeste(self,_oeste):
        self.oeste=_oeste

    @property
    def orientaciones(self):
        return self.orientaciones

    @orientaciones.setter
    def orientaciones(self,_orientaciones):
        self.orientaciones=_orientaciones

    def ponerEnElemento(unaOrientacion,unEM):
        unaOrientacion.ponerElementoEn(unEM,self)

    def recorrer(unBloque):
        unBloque.value(self)
        for x in hijos:
            x.recorrer(unBloque)
        for y in orientaciones:
            y.recorrerEn(unBloque,self)

    @property
    def sur(self):
        return self.sur

    @sur.setter
    def sur(self,_sur):
        self.sur=_sur