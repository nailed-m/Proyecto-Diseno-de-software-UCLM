#!/usr/bin/python
#-*- coding: utf-8 -*-

class Bicho():
    def __init__(self):
        self.modo=None
        self.poder=None
        self.posicion=None
        self.vidas=None
        
    def actua():
        self.modo.actua(self)

    def esAgresivo():
        return self.modo.esAgresivo()

    def esPerezoso():
        return self.modo.esPerezoso()
    
    def estaVivo():
        if self.vidas(self) > 0:
            return True
        else:
            return False
    
    def irA(unaOr):
        unaOr.ir(self)
    
    @property
    def modo(self):
        return self.modo

    @modo.setter
    def modo(self, _modo):
        self.modo=_modo

    def muere():
        print("Bicho " + self.modo(self) + " muere")
        self.vidas(self,0)

    def obtenerOrientacionAleatoria():
        return self.posicion(self).obtenerOrientacionAleatoria()

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
    
    def printOn(aStream):
        aStream = "Bicho-" + self.modo(self)

    def quitarVidas(unNum):
        self.vidas(self,self.vidas(self)-unNum)

    @property
    def vidas(self):
        return self.vidas
    
    @vidas.setter
    def vidas(self, _vidas):
        self.vidas=_vidas
