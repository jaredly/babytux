#!/usr/bin/env python

from random import uniform

from pyglet import clock, font, image, window
from pyglet.gl import *

import app,world,sprite,camera

class Triangle(sprite.Sprite):
    
    def __init__(self, x, y, size, rot):
        self.x = x
        self.y = y
        self.size = size
        self.rot = rot

    def step(self):
        self.rot += 10.0/self.size

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


class Main(app.App):
    def __init__(self):
        super(Main, self).__init__()
        clock.schedule_interval(self.new_triangle, 0.25)

    def new_triangle(self, dt):
        x = uniform(-100.0, 100.0)
        y = uniform(-100.0, 100.0)
        size = uniform(1.0, 100.0)
        rot = uniform(0.0, 360.0)
        tri = Triangle(x, y, size, rot)
        self.world.objects.append(tri)




if __name__=='__main__':
    app = Main()
    app.mainLoop()


# vim: et sw=4 sts=4
