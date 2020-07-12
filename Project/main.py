import pygame
import pygame_gui
import math
import os
from tank import Tank
from player import Player
from request import RequestServer


directory = str(os.path.abspath(os.getcwd())) + '/' # + '/Project/'


pygame.init()
pygame.display.set_caption("Tanksta")
screen = pygame.display.set_mode((1600, 900))
background = pygame.image.load(directory + 'assets/background2.png')
background = pygame.transform.scale(background, (1600, 900))


tanks = [Tank((350,650)),
    Tank((900,650))]

player = Player(tanks[0])
running = True
game_start = False

server = RequestServer()
manager = pygame_gui.UIManager((1600, 900))
clock = pygame.time.Clock()
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((750, 175), (100, 50)),
                                             text='Play Online',
                                             manager=manager)

while running:
    pygame.display.flip()
    time_delta = clock.tick(60)/1000.0
    screen.blit(background, (0, 0))
    
    if game_start:
        for tank in tanks:
            tank.display(screen, tanks)
        
        player.wait()
        for i in range(len(tanks)):
            if i >= len(tanks):
                i = len(tanks) - 1
            if tanks[i].health <= 0:
                del tanks[i] 

        if len(tanks) == 1:
            pygame.quit()
            print("Game Closed")
            running = False
    
    for event in pygame.event.get():
        if game_start:
            player.controller(event)
        manager.process_events(event)
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == hello_button:
                    server.wantToPlay()
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Game Closed")
            running = False
    
    server.checkGameIsFind()
    manager.update(time_delta)
    manager.draw_ui(screen)
   
    