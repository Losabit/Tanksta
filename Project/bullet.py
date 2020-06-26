import pygame
import os
import math

directory = str(os.path.abspath(os.getcwd()))  + '/Project/'

class Bullet(pygame.sprite.Sprite):
    def __init__(self, coordonates, angle, puissance):
        self.image = pygame.image.load(directory + 'assets/objects/tank_bullet5.png')
        self.origin_image = self.image
        self.rect = coordonates
        self.image = pygame.transform.rotate(self.origin_image, angle)
        self.angle = angle
        self.puissance = puissance
        self.before_rect_y = ((-9.81 * math.pow(self.rect[0], 2)) / (2 * math.pow(self.puissance * math.cos(math.radians(self.angle)), 2)) + self.rect[0] * math.tan(math.radians(self.angle)))
        self.altitude_max = math.pow(self.puissance * math.sin(math.radians(self.angle)), 2) / (2 * 9.81) + self.rect[1]
        self.chute = False

    def display(self, screen):
        screen.blit(self.image, self.rect)
        self.fire()

    def fire(self):
        self.rect[0] += self.puissance
        rect_y = ((-9.81 * math.pow(self.rect[0], 2)) / (2 * math.pow(self.puissance * math.cos(math.radians(self.angle)), 2)) + self.rect[0] * math.tan(math.radians(self.angle)))
        
        if self.rect[1] > self.altitude_max:
            self.chute = True
        if self.chute:
            self.rect[1] -= (rect_y - self.before_rect_y) / 1000
        else:
            self.rect[1] += (rect_y - self.before_rect_y) / 1000
        
        self.before_rect_y = rect_y
        print(self.rect[1])
        print(self.altitude_max )