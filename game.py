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

    def on_key_press(self, symbol, mods):

        if symbol == pyglet.window.key.ESCAPE:
            sys.exit(0)
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
        self.add(x, y)

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
