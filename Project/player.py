import pygame
import os
from tank import Tank

min_puissance = 1
max_puissance = 10
value_puissance = 0.05
ecart_angle = 20

class Player():
    def __init__(self, Tank):
        self.tank = Tank
        self.puissance = min_puissance
        self.increase_puissance = False

    def wait(self):
        if self.increase_puissance:
            self.puissance += value_puissance

    def controller(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               self.increase_puissance = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print(self.puissance)
                self.tank.shoot(self.puissance if self.puissance < max_puissance else max_puissance)
                self.puissance = min_puissance
                self.increase_puissance = False

            if event.key == pygame.K_q and self.tank.canon_angle < 180 + ecart_angle:
                self.tank.moveCanon(10)
            elif event.key == pygame.K_d and self.tank.canon_angle > -ecart_angle:
                self.tank.moveCanon(-10)

            if event.key == pygame.K_RIGHT:
                self.tank.move(20)
            elif event.key == pygame.K_LEFT:
                self.tank.move(-20)