#!/usr/bin/env python

from sprite import Sprite
import rabbyt
import pyglet
from pyglet.gl import *

class SImage(Sprite):

    def __init__(self, image, x, y):
        self.sp = rabbyt.Sprite(image)
        self.sp.x = x
        self.sp.y = y

    def draw(self):
        glEnable(GL_BLEND)
        self.sp.render()

    def step(self):
        self.sp.rot += 10
        pass

class SImageStatic(SImage):
    def __init__(self, *a):
        SImage.__init__(self, *a)

    def step(self):
        return

