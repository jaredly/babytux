#!/usr/bin/env python

import pyglet
from pyglet.gl import *

class App(object):

    def __init__(self):
        self.world = World()
        self.win = window.Window(fullscreen=False, vsync=True)

        self.win.on_mouse_drag = self.on_mouse_drag
        self.win.on_mouse_motion = self.on_mouse_motion
        self.win.on_mouse_press = self.on_mouse_press
        self.win.on_mouse_release = self.on_mouse_release

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
            self.win.dispatch_events()

            self.world.tick()

            self.camera.worldProjection()
            self.world.draw()

            self.camera.hudProjection()
            self.hud.draw()

            clock.tick()
            self.win.flip()




# vim: et sw=4 sts=4
