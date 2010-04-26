#!/usr/bin/env python

import pyglet
from pyglet.gl import *

class World(object):

    def __init__(self):
        self.objects = []

    def spawnEntity(self, dt):
        size = uniform(1.0, 100.0)
        x = uniform(-100.0, 100.0)
        y = uniform(-100.0, 100.0)
        rot = uniform(0.0, 360.0)
        ent = Entity(self.nextEntId, size, x, y, rot)
        self.ents[ent.id] = ent
        self.nextEntId += 1
        return ent

    def step(self):
        for obj in self.objects:
            obj.step()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        for obj in self.objects:
            obj.draw()

# vim: et sw=4 sts=4
