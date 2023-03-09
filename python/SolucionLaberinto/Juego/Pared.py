#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Pared(ElementoMapa):
    def entrar():
        print("Te has chocado con una pared")

    def esPared():
        return True
