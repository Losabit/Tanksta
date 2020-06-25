import pygame
import math
import os
from tank import Tank
from player import Player


directory = str(os.path.abspath(os.getcwd()))  + '/Project/'


pygame.init()
pygame.display.set_caption("Tanksta")
screen = pygame.display.set_mode((1600, 900))
background = pygame.image.load(directory + 'assets/background2.png')
background = pygame.transform.scale(background, (1600, 900))


tank = Tank((350,650))
player = Player(tank)
running = True

while running:
    screen.blit(background, (0, 0))
    tank.display(screen)
    pygame.display.flip()
    player.wait()
    
    for event in pygame.event.get():
        player.controller(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Game Closed")
            running = False
       