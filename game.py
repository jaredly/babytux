#!/usr/bin/env python

import random
import rabbyt
import simage
import math
import time
import app

from pyglet import clock

#rabbyt.set_default_attribs()

def normal(ang):
    ang %= 360
    if ang > 180:
        ang -= 360
    return ang

class SImage(simage.SImage):
    def __init__(self, *a):
        simage.SImage.__init__(self, *a)
        self.speed = 3
        self.d = 0
        self.gd = 0

    def step(self):
        return
        self.sp.x += math.cos(self.d) * self.speed
        self.sp.y += math.sin(self.d) * self.speed

        diff = normal(self.gd - self.d)
        if abs(diff) < 10:
            self.gd = random.uniform(0, 360)
        else:
            self.d += diff/1000.0


class Main(app.App):
    def __init__(self):
        super(Main, self).__init__()
        #clock.schedule_interval(self.new_triangle, 0.25)
        clock.schedule(rabbyt.add_time)

        '''
        self.pos = 0,0
        w = self.win.width/10.0
        h = self.win.height/10.0
        for i in range(11):
            s = SImage('ring.png', i*w, i*h)
            self.world.objects.append(s)
            '''

    def on_mouse_press(self, x, y, button, mods):
        self.pos = x,y

    def on_mouse_drag(self, x, y, dx, dy, buttons, mods):
        if dst(x-self.pos[0], y-self.pos[1]) > 15:
            self.add(x,y)
            self.pos = x,y

    def add(self, x, y):
        s = SImage('ring.png', x, y)
        s.sp.scale = rabbyt.lerp(start=.1, end=2, dt=1)
        s.sp.alpha = rabbyt.lerp(end=0, dt=1)
        self.world.objects.append(s)
        clock.schedule_once(lambda dt:self.world.objects.remove(s), 1)
        '''
        s.sp.scale = rabbyt.lerp(start=.5, end=1.0, dt=.5, extend='reverse')
        def tmp(dt):
            s.sp.scale = rabbyt.lerp(end=5.0, dt=.3)
            s.sp.alpha = rabbyt.lerp(start=1.0, end=0, dt=.3)
            clock.schedule_once(lambda dt:self.world.objects.remove(s), .3)
        clock.schedule_once(tmp, 1)
        '''

    def step(self):
        pass

def dst(x,y):
    return math.sqrt(x**2+y**2)

if __name__=='__main__':
    Main().mainLoop()

# vim: et sw=4 sts=4
