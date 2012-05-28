#!/usr/bin/env python

import string, math, time, sys, random

from simage import SImage, SImageStatic
from sprite import SpriteText
from firework import FireWork
import app

import rabbyt
import pyglet
from pyglet import clock, font

def normal(ang):
    ang %= 360
    if ang > 180:
        ang -= 360
    return ang


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

        try:
            s = chr(symbol)
        except (ValueError, OverflowError):
            # Deal with <ENTER>, <ESC>, <SHIFT>, <F1-F12>, <ALT>, unicode
            # character, etc. For our purpose, change it to a period
            s = '.'
            pass

        if s in string.ascii_letters:
            self.make_string(s.upper())
        elif s in string.digits:
            self.make_string(s)
        else: # work with our ValueError and if user enters space, puncutations, etc
            self.make_shape_animations()

    def make_string(self, string):
        x, y = get_xy_positions(self.win.width, self.win.height)
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

    def make_shape_animations(self):
        x, y = get_xy_positions(self.win.width, self.win.height)
        s = SImage(get_random_image(), x, y)
        s.sp.x = rabbyt.lerp(end=random.uniform(0, self.win.width), dt=1)
        s.sp.y = rabbyt.lerp(end=random.uniform(0, self.win.height), dt=1)
        s.sp.rot = rabbyt.lerp(start=0, end=360, dt=1)
        s.sp.scale = rabbyt.lerp(.25, 1, dt=1)
        self.world.objects.append(s)
        clock.schedule_once(lambda dt:self.world.objects.remove(s), 1)


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
        s = SImageStatic('res/ring.png', x, y)
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

def get_xy_positions(width, height):
    return random.uniform(0, width), random.uniform(0, height)

def get_random_image():
    choice = random.randint(1, 3)
    if choice == 1:
        return 'res/circle.png'
    elif choice == 2:
        return 'res/triangle.png'
    else:
        return 'res/square.png'

if __name__=='__main__':
    Main().mainLoop()

