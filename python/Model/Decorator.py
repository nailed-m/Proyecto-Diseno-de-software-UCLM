#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa

class Decorator(ElementoMapa):

    def __init__(self):
        self.activa = None

    @property
    def component(self):
        return self.component

    @component.setter
    def component(self, _component):
        self.component=_component
