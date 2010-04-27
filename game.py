#!/usr/bin/env python

import random
import rabbyt
import simage
import sprite

import string
import math
import time
import sys

import app

import pyglet
from pyglet import clock, font

def normal(ang):
    ang %= 360
    if ang > 180:
        ang -= 360
    return ang

class SImage(simage.SImage):
    def __init__(self, *a):
        simage.SImage.__init__(self, *a)

    def step(self):
        return


class FireWork(sprite.Sprite):
    def __init__(self, x, y):
        dst = 50
        num = 10
        dt = .6
        fscale = 1
        by = 360.0/num
        self.images = []
        for i in range(num):
            ang = i*by
            rad = ang / 180.0 * math.pi
            s = simage.SImage('wedge.png', x, y)
            s.sp.x = rabbyt.lerp(end=math.cos(rad)*dst*fscale+x, dt=dt)
            s.sp.y = rabbyt.lerp(end=math.sin(rad)*dst*fscale+y, dt=dt)
            '''cool things:
            #1
            s.sp.rot = ang - 90

            #2
            s.sp.rot = ang

            #3
            s.sp.rot = ang + 90
            '''
            s.sp.rot = rabbyt.lerp(ang, ang - 90.0, dt=dt/2)
            s.sp.rot = rabbyt.lerp(ang + 90, ang - 90.0, dt=dt)
            #s.sp.rot = ang - 90.0
            s.sp.scale = rabbyt.lerp(0,fscale,dt=dt)
            self.images.append(s)
        self.on = True
        def tmp(dt):
            l = rabbyt.lerp(1.0,0.0,dt=dt)
            for i in self.images:
                i.sp.alpha = l#rabbyt.lerp(1.0,0.0,dt=1)
            clock.schedule_once(self.off, dt)
        clock.schedule_once(tmp, dt/2)

    def off(self, dt):
        self.on = False

    def draw(self):
        if not self.on:return
        for i in self.images:
            i.draw()

class SpriteText(rabbyt.BaseSprite):
    def __init__(self, ft, text="", *args, **kwargs):
        rabbyt.BaseSprite.__init__(self, *args, **kwargs)
        self._text = font.Text(ft, text,
            halign=font.Text.CENTER,
            valign=font.Text.CENTER,
            )

    def set_text(self, text):
        self._text.text = text

    def render_after_transform(self):
        self._text.color = self.rgba
        self._text.draw()

    def draw(self):
        self.render()

    def step(self):
        pass

class Main(app.App):
    def __init__(self):
        super(Main, self).__init__()
        clock.schedule(rabbyt.add_time)
        self.ft = font.load('Helvetica', self.win.width/20)
        self.pos = 0,0
        self.key_buffer = []

    def on_key_press(self, symbol, mods):
        self.key_buffer.append(symbol)
        self.key_buffer = self.key_buffer[-6:]

        code = 'smash'
        if len(self.key_buffer) == 6:
            for key, char in zip(self.key_buffer, code):
                if key != ord(char):
                    break
            else:
                if self.key_buffer[-1] == pyglet.window.key.ESCAPE:
                    sys.exit(0)
        #if symbol == pyglet.window.key.ESCAPE:
        #    sys.exit(0)
        try:
            s = chr(symbol)
        except (ValueError, OverflowError):
            return
        if s in string.ascii_letters:
            self.make_string(s.upper())

    def make_string(self, string):
        x = random.uniform(0, self.win.width)
        y = random.uniform(0, self.win.height)
        s = SpriteText(self.ft, string)
        s.rgba = rcolor()
        s.x = rabbyt.lerp(x, random.uniform(0, self.win.width), dt=1)
        s.y = rabbyt.lerp(y, random.uniform(0, self.win.height), dt=1)
        s.rot = rabbyt.lerp(start=0, end=360, dt=1)
        s.scale = rabbyt.lerp(.5, 1, dt=1)
        self.world.objects.append(s)
        def tmp(dt):
            s.alpha = rabbyt.lerp(1.0, 0, dt=2)
            clock.schedule_once(lambda dt:self.world.objects.remove(s),2)
        clock.schedule_once(tmp, 2)

    def on_mouse_press(self, x, y, button, mods):
        self.pos = x,y
        self.world.objects.append(FireWork(x,y))

    def on_mouse_drag(self, x, y, dx, dy, buttons, mods):
        if dst(x-self.pos[0], y-self.pos[1]) > 15:
            self.add(x,y)
            self.pos = x,y

    def on_mouse_motion(self, x, y, buttons, mods):
        if dst(x-self.pos[0], y-self.pos[1]) > 15:
            self.add(x,y)
            self.pos = x,y

    def add(self, x, y):
        s = SImage('ring.png', x, y)
        s.sp.scale = rabbyt.lerp(start=.1, end=2, dt=1)
        s.sp.alpha = rabbyt.lerp(end=0, dt=1)
        self.world.objects.append(s)
        clock.schedule_once(lambda dt:self.world.objects.remove(s), 1)

    def step(self):
        pass

def rcolor():
    return tuple(random.uniform(0,255) for i in (0,0,0)) + (1,)

def dst(x,y):
    return math.sqrt(x**2+y**2)

if __name__=='__main__':
    Main().mainLoop()

# vim: et sw=4 sts=4
