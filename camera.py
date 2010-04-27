#!/usr/bin/env python

import pyglet
from pyglet.gl import *

class Camera(object):

    def __init__(self, win, x=0.0, y=0.0, rot=0.0, zoom=100.0):
        self.win = win
        self.x = x
        self.y = y
        self.rot = rot
        self.zoom = zoom

    def worldProjection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        widthRatio = self.win.width / self.win.height
        look = 0, self.win.width, 0, self.win.height
        look = self.scale(look, 1)
        gluOrtho2D(*look)
        glMatrixMode(GL_MODELVIEW)
        '''
            -self.zoom * widthRatio,
            self.zoom * widthRatio,
            -self.zoom,
            self.zoom)
        '''

    def scale(self, look, scale):
        w = look[1]-look[0]
        h = look[3]-look[2]
        m = (look[1]+look[0])/2.0, (look[3]+look[2])/2.0
        return m[0] - w*scale/2, m[0] + w*scale/2, m[1] - h*scale/2, m[1] + h*scale/2



    def hudProjection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, self.win.width, 0, self.win.height)


# vim: et sw=4 sts=4
