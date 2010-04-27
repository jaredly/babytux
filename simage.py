#!/usr/bin/env python

import rabbyt
import sprite
import pyglet
from pyglet.gl import *

class SImage(sprite.Sprite):

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


# vim: et sw=4 sts=4
