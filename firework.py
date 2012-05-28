import random, math
import rabbyt
from simage import SImage
from sprite import Sprite
from pyglet import clock

class FireWork(Sprite):
    def __init__(self, x, y):
        dst = 50
        num = 10
        dt = .6
        fscale = 1
        by = 360.0/num
        choice = random.randint(1, 5)
        self.images = []
        for i in range(num):
            ang = i*by
            rad = ang / 180.0 * math.pi
            s = SImage('res/wedge.png', x, y)
            s.sp.x = rabbyt.lerp(end=math.cos(rad)*dst*fscale+x, dt=dt)
            s.sp.y = rabbyt.lerp(end=math.sin(rad)*dst*fscale+y, dt=dt)
            s.sp.rot = get_rotation(choice, ang, dt)
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

def get_rotation(choice, ang, dt):
    if choice == 1:
        return ang - 90
    elif choice == 2:
        return ang
    elif choice == 3:
        return ang + 90
    elif choice == 4:
        return rabbyt.lerp(ang, ang - 90.0, dt=dt/2)
    else: 
        return rabbyt.lerp(ang + 90, ang - 90.0, dt=dt/2)

