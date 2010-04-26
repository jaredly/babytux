#!/usr/bin/env python

import pyglet
from pyglet import *

class Entity(object):

    def __init__(self, id, size, x, y, rot):
        self.id = id
        self.size = size
        self.x = x
        self.y = y
        self.rot = rot

    def draw(self):
        glLoadIdentity()
        glTranslatef(self.x, self.y, 0.0)
        glRotatef(self.rot, 0, 0, 1)
        glScalef(self.size, self.size, 1.0)
        glBegin(GL_TRIANGLES)
        glColor4f(1.0, 0.0, 0.0, 0.0)
        glVertex2f(0.0, 0.5)
        glColor4f(0.0, 0.0, 1.0, 1.0)
        glVertex2f(0.2, -0.5)
        glColor4f(0.0, 0.0, 1.0, 1.0)
        glVertex2f(-0.2, -0.5)
        glEnd()


# vim: et sw=4 sts=4
