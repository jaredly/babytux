#!/usr/bin/env python

import pyglet, sys
from pyglet import window, clock, font, image
from pyglet.gl import *

from world import World
from camera import Camera

class Hud(object):

    def __init__(self, win):
        helv = font.load('Helvetica', win.width / 15.0)
        self.text = font.Text(
            helv,
            'Hello!',
            x=win.width / 2,
            y=win.height / 2,
            halign=font.Text.CENTER,
            valign=font.Text.CENTER,
            color=(1, 1, 1, 0.5),
        )
        h = font.load('Helvetica', 15)
        self.help = font.Text(h, 'to exit: type "smash" and press escape', x=10, y=win.height-25, color=(1,1,1,.5))
        self.fps = clock.ClockDisplay()

    def draw(self):
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        self.text.draw()
        self.help.draw()
        if __debug__: self.fps.draw()

class App(object):

    def __init__(self):
        self.world = World()
        self.win = pyglet.window.Window(fullscreen=True, vsync=True)

        for i in dir(self):
            if i.startswith('on_'):
                setattr(self.win, i, getattr(self, i))

        self.camera = Camera(self.win, zoom=100.0)
        self.hud = Hud(self.win)
        clock.set_fps_limit(60)

    def on_mouse_drag(self, x, y, dx, dy, buttons, mods):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_press(self, x, y, button, mods):
        pass

    def on_mouse_release(self, x, y, button, mods):
        pass

    def mainLoop(self):
        while not self.win.has_exit:
            try:
                self.win.dispatch_events()

                self.world.step()

                self.camera.worldProjection()
                self.world.draw()

                self.camera.hudProjection()
                self.hud.draw()

                clock.tick()
                self.win.flip()
            except (SystemExit):
                sys.exit(0)
            except:
                pass
