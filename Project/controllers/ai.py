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
            self.tank.move(-random.randint(1,60))
        if random.randint(1, 1000) < 60:
            self.tank.moveCanon(-random.randint(1,90))
            self.tank.shoot(self.puissance if self.puissance < max_puissance else max_puissance)
            self.puissance = random.randint(1,20)
            self.increase_puissance = False


    def predictAngle(self, Tank):
        deltaX = self.Tank.body_rect[0] - Tank.body_rect[0]
        deltaY = self.Tank.body_rect[1] - Tank.body_rect[1]
        deg = math.atan2(deltaY,deltaX) * (180 / math.pi)
        return deg

        '''
        if event.key == pygame.K_q:
            self.can_move_canon = True
            self.canon_direction = 1
        elif event.key == pygame.K_d:
            self.can_move_canon = True
            self.canon_direction = -1

        if event.key == pygame.K_q and self.tank.canon_angle < 180 + ecart_angle:
            self.can_move_canon = False
        elif event.key == pygame.K_d and self.tank.canon_angle > -ecart_angle:
            self.can_move_canon = False
        '''

    def basic_controller(self, tank, tanks_ennemies):    
        self.increase_puissance = True
        if random.randint(1, 1000) < 60:
            self.tank.shoot(self.puissance if self.puissance < max_puissance else max_puissance)
            self.puissance = min_puissance
            self.increase_puissance = False
