#!/usr/bin/python
#-*- coding: utf-8 -*-

class Laberinto:
    def __init__(self):
        self.habitaciones = list()

    def agregarHabitacion(self,unaHab):
        self.habitaciones.append(unaHab)

    @property
    def habitaciones(self):
        return self.habitaciones

    @habitaciones.setter
    def habitaciones(self,_habitaciones):
        self.habitaciones=_habitaciones

    def obtenerHabitacion(self,unNum):
        return self.habitaciones[unNum]
