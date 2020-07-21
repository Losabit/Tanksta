import pygame
import os
from tank import Tank
from controller import Controller

min_puissance = 2
max_puissance = 10
ecart_angle = 15

class Player(Controller):
    def __init__(self, Tank):
        Controller.__init__(self, Tank)

    def controller(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               self.increase_puissance = True

            if event.key == pygame.K_q:
                self.can_move_canon = True
                self.canon_direction = 1
            elif event.key == pygame.K_d:
                self.can_move_canon = True
                self.canon_direction = -1

            if event.key == pygame.K_RIGHT and self.move == False:
                self.move = True
                self.direction = 1
            elif event.key == pygame.K_LEFT and self.move == False:
                self.move = True
                self.direction = -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.tank.shoot(self.puissance if self.puissance < max_puissance else max_puissance)
                self.puissance = min_puissance
                self.increase_puissance = False

            if event.key == pygame.K_q and self.tank.canon_angle < 180 + ecart_angle:
                self.can_move_canon = False
            elif event.key == pygame.K_d and self.tank.canon_angle > -ecart_angle:
                self.can_move_canon = False

            if event.key == pygame.K_RIGHT and self.direction > 0:
                self.move = False
            elif event.key == pygame.K_LEFT and self.direction < 0:
                self.move = False