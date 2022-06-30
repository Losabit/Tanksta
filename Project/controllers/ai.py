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
            self.tank.moveCanon(self.predictAngle(self.tank.canon_angle,tank))
            self.tank.shoot(self.puissance if self.puissance < max_puissance else max_puissance)
            self.puissance = random.randint(1, 20)
            self.increase_puissance = False

    def predictAngle(self,canon_angle, tank):
        if self.tank.body_rect[0] > tank.body_rect[0]:
            if canon_angle == -200:
                return 0
            else:
                deg = -200
        else:
            if canon_angle == 200:
                return 0
            else:
                deg = 200
        return deg

<<<<<<< HEAD
=======
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

>>>>>>> 478731d5a7284ef25c807c3b9ca94acaed3bbf50
    def basic_controller(self, tank, tanks_ennemies):
        self.increase_puissance = True
        if random.randint(1, 1000) < 60:
            self.tank.shoot(self.puissance if self.puissance < max_puissance else max_puissance)
            self.puissance = min_puissance
            self.increase_puissance = False
