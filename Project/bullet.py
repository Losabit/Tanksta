import pygame
import os
import math

directory = str(os.path.abspath(os.getcwd())) + '/' #'/Project/'

class Bullet(pygame.sprite.Sprite):
    def __init__(self, coordonates, angle, puissance):
        self.image = pygame.image.load(directory + 'assets/objects/tank_bullet5.png')
        self.origin_image = self.image
        self.rect = coordonates
        self.image = pygame.transform.rotate(self.origin_image, angle)
        self.angle = angle
        self.damage = 20
        self.puissance = puissance
        self.altitude_max = self.rect[1] - 650 * math.sin(math.radians(self.angle)) 
        self.altitude_start = self.rect[1]
        self.chute = False
        '''
        print("angle : " + str(self.angle))
        print("puissance : " + str(self.puissance))
        print(self.rect[0])
        print("altitude max : " + str(self.altitude_max))
        '''

    def display(self, screen):
        screen.blit(self.image, self.rect)
        self.fire()

    def fire(self):
        self.rect[0] += self.puissance * math.cos(math.radians(self.angle)) 
        
        if self.rect[1] < self.altitude_max:
            self.chute = True
            self.rect[1] = self.altitude_max

        #coeff = 1 - math.sin((self.rect[1] * math.pi / 2) / self.altitude_max)
        if self.chute:
            self.rect[1] += self.puissance * math.sin(math.radians(abs(self.angle))) 
        else:
            self.rect[1] -= self.puissance * math.sin(math.radians(self.angle))
        