import pygame
import os
import math
import random
from tank import Tank
from controller import Controller

min_puissance = 4
max_puissance = 10
value_puissance = 0.05
ecart_angle = 15
canon_angle_value = 2
move_value = 3


class AI(Controller):
    def __init__(self, Tank):
        Controller.__init__(self, Tank)

    def random_controller(self, tank):
        self.increase_puissance = True
        if random.randint(1, 1000) < 30:
            self.tank.move(-random.randint(1, 60))
        if random.randint(1, 1000) < 60:
            self.tank.moveCanon(self.predictAngle(tank))
            self.tank.shoot(self.puissance if self.puissance < max_puissance else max_puissance)
            self.puissance = random.randint(1, 20)
            self.increase_puissance = False

    def predictAngle(self, tank):
        deltaX = self.tank.body_rect[0] - tank.body_rect[0]
        print(deltaX)
        deltaY = self.tank.body_rect[1] - tank.body_rect[1]
        deg = math.atan2(deltaY, deltaX) * (180 / math.pi)
        if self.tank.body_rect[0] > tank.body_rect[0]:
            deg = (deg - 180) % -360
        return deg

    def basic_controller(self, tank, tanks_ennemies):
        self.increase_puissance = True
        if random.randint(1, 1000) < 60:
            self.tank.shoot(self.puissance if self.puissance < max_puissance else max_puissance)
            self.puissance = min_puissance
            self.increase_puissance = False
