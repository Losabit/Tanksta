import pygame
import os
from tank import Tank

min_puissance = 4
max_puissance = 10
value_puissance = 0.05
ecart_angle = 15
canon_angle_value = 2
move_value = 3

class Controller():
    def __init__(self, Tank):
        self.tank = Tank
        self.puissance = min_puissance
        self.increase_puissance = False
        self.move = False
        self.direction = 0
        self.can_move_canon = False
        self.canon_direction = 0


    def update(self):
        if self.increase_puissance:
            self.puissance += value_puissance
        if self.move and self.direction != 0:
            self.tank.move(move_value if self.direction > 0 else -move_value)
        if self.can_move_canon and self.canon_direction != 0:
            if self.canon_direction > 0 and self.tank.canon_angle > 180 + ecart_angle:
                return
            if self.canon_direction < 0 and self.tank.canon_angle < -ecart_angle:
                return
            self.tank.moveCanon(canon_angle_value if self.canon_direction > 0 else -canon_angle_value)
    
    def stop(self):
        self.puissance = min_puissance
        self.move = False
        self.can_move_canon = False
        self.increase_puissance = False
    
    '''
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
    '''