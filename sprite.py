#!/usr/bin/env python

import rabbyt
import pyglet 
from pyglet import font
from pyglet.gl import *
import random, math

class Sprite(object):
    def __init__(self, x, y, rot):
        pass

    def draw(self):
        pass

    def step(self):
        pass

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


