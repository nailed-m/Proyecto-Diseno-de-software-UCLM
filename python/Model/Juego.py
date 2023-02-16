#!/usr/bin/python
#-*- coding: utf-8 -*-

from Habitacion import Habitacion
from Laberinto import Laberinto
from Puerta import Puerta
from Pared import Pared
from Bicho import Bicho
from Bomba import Bomba
from Agresivo import Agresivo
from Perezoso import Perezoso

class Juego:
    def __init__(self):
        self.bichos=list()
        self.laberinto=None

    def agregarBicho(self,unBicho):
        hab=self.obtenerHabitacion(1)
        unBicho.posicion(unBicho,hab)
        self.bichos.add(unBicho)

    @property
    def bichos(self):
        return self.bichos

    @bichos.setter
    def bichos(self,anObject):
        self.bichos=anObject

    def fabricarBichoAgresivoPosicion(self,unaHab):
        bicho=Bicho()
        bicho.modo(bicho,self.fabricarModoAgresivo())
        bicho.vidas(bicho,10)
        bicho.poder(bicho,10)
        bicho.posicion(unaHab)
        return bicho

    def fabricarBichoPerezosoPosicion(self,unaHab):
        bicho=Bicho()
        bicho.modo(bicho,self.fabricarModoPerezoso())
        bicho.vidas(bicho,10)
        bicho.poder(bicho,10)
        bicho.posicion(unaHab)
        return bicho

    def fabricarBomba():
        return Bomba()

    def fabricarHabitacion(unNum):
        hab=Habitacion(unNum)
        return hab

    def fabricarLaberinto(self):
        return Laberinto()

    def fabricarModoAgresivo():
        return Agresivo()

    def fabricarModoPerezoso():
        return Perezoso()

    def fabricarPared():
        return Pared()

    def fabricarPuerta(unaHab,otraHab):
        puerta=Puerta()
        puerta.lado1(puerta,unaHab)
        puerta.lado2(puerta,otraHab)
        return puerta

    @property
    def laberinto(self):
        return self.laberinto

    @laberinto.setter
    def laberinto(self,_laberinto):
        self.laberinto=_laberinto

    def laberinto2Habitaciones(self):
        self.laberinto(self,Laberinto())

        hab1 = Habitacion(1)
        hab2 = Habitacion(2)

        puerta = Puerta()
        puerta.lado1(puerta,hab1)
        puerta.lado2(puerta,hab2)

        hab1.sur(hab1,puerta)
        hab2.norte(hab2,puerta)

        hab1.norte(hab1,Pared())
        hab1.este(hab1,Pared())
        hab1.oeste(hab1,Pared())

        hab2.sur(hab2,Pared())
        hab2.este(hab2,Pared())
        hab2.oeste(hab2,Pared())

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def laberinto2HabitacionFM(self):
        self.laberinto(self,self.fabricarLaberinto())

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)

        puerta = self.fabricarPuerta(hab1,hab2)

        hab1.norte(hab1,self.fabricarPared())
        hab1.este(hab1,self.fabricarPared())
        hab1.oeste(hab1,self.fabricarPared())

        hab2.sur(hab2,self.fabricarPared())
        hab2.este(hab2,self.fabricarPared())
        hab2.oeste(hab2,self.fabricarPared())

        hab1.sur(hab1,puerta)
        hab2.norte(hab2,puerta)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def laberinto2HabitacionesFMD(self):
        self.laberinto(self,self.fabricarLaberinto())

        bm1 = self.fabricarBomba()
        bm1.component(bm1,self.fabricarPared())
        bm2 = self.fabricarBomba()
        bm2.component(bm2,self.fabricarPared())

        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)

        puerta = self.fabricarPuerta(hab1,hab2)

        hab1.norte(hab1,bm1)
        hab1.oeste(hab1,self.fabricarPared)
        hab1.este(hab1,self.fabricarPared)

        hab2.sur(hab2,bm2)
        hab2.oeste(hab2,self.fabricarPared)
        hab2.este(hab2,self.fabricarPared)

        hab1.sur(hab1,puerta)
        hab2.norte(hab2,puerta)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

    def obtenerHabitacion(self,unNum):
        return self.laberinto.obtenerHabitacion(unNum)
        
juego=Juego()
juego.laberinto2Habitaciones()
