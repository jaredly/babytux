#!/usr/bin/env python

from random import uniform
import math

import rabbyt

from pyglet import clock, font, image, window
from pyglet.gl import *

import app,world,sprite,camera

class Image(sprite.Sprite):
    def __init__(self, image, x, y, size):
        self.x=x
        self.y=y
        self.size=size
        self.image = pyglet.image.load(image)

    def draw(self):
        self.image.blit(self.x, self.y, 0)

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

        glColor4f(1.0, 0.0, 0.0, 0.0)
        pyglet.graphics.draw_indexed(3, pyglet.gl.GL_TRIANGLES,
                [0, 1, 2],
                ('v2f', (0.0, 0.5,
                         0.2, -0.5,
                        -0.2, -0.5))
            )

        '''
        glBegin(GL_TRIANGLES)
        glVertex2f(0.0, 0.5)
        glColor4f(0.0, 0.0, 1.0, 1.0)
        glVertex2f(0.2, -0.5)
        glColor4f(0.0, 0.0, 1.0, 1.0)
        glVertex2f(-0.2, -0.5)
        glEnd()
        '''

class Circle(sprite.Sprite):

    def __init__(self, x, y, rad, color, lw, lc):
        self.x = x
        self.y = y
        self.z = 0
        self.rad = rad
        self.color = color
        self.lw = lw
        self.lc = lc
        self.q = gluNewQuadric()

        self.tick = 0

    def step(self):
        self.tick += 30
        self.z = math.sin(math.pi * self.tick/180.0)

    def draw(self):
        
        glColor4f(*self.color)
        glPushMatrix()

        glTranslatef(self.x, self.y, -self.z)
        #glRotatef(self.rot, 0, 0, 0.1)

        if self.rad< 1 : self.rad= 1
        '''
        if self.lw:
            inner = self.rad- self.lw # outline width
            if inner < 0: inner=0
        else:
             inner = 0 # filled
        '''
        
        gluQuadricDrawStyle(self.q, GLU_FILL)# self.style)
        gluDisk(self.q, 0, self.rad, 60, 1) # gluDisk(quad, inner, outer, slices, loops)
        glPopMatrix()

class Main(app.App):
    def __init__(self):
        super(Main, self).__init__()
        clock.schedule_interval(self.new_triangle, 0.25)

        #car = SImage('ring.png',0,0)
        #self.world.objects.append(car)

        w = self.win.width/10.0
        h = self.win.height/10.0
        for i in range(11):
            s = SImage('ring.png', i*w, i*h)
            self.world.objects.append(s)

    def new_triangle(self, dt):
        return
        if len(self.world.objects)>20:return

        x = uniform(0.0, self.win.width/2)
        y = uniform(0.0, self.win.height/2)
        size = uniform(1.0, 100.0)
        rot = uniform(0.0, 360.0)
        tri = pyglet.sprite.Sprite(self.rimg, x, y)
        tri.step = lambda:None
        #tri = Image('ring.png', x, y, size)
        #tri = Triangle(x, y, size, rot)
        #tri = Circle(x, y, size, (100,200,0,1), 0, 0)#Triangle(x, y, size, rot)
        self.world.objects.append(tri)




if __name__=='__main__':
    app = Main()
    app.mainLoop()


# vim: et sw=4 sts=4
