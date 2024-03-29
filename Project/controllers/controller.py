import pygame
import os
import sys
from tank import Tank

min_puissance = 2
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

    # Update the tank's position and angle of canon
    def update(self):
        if self.increase_puissance:
            print("Increasing power", self.puissance)
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
