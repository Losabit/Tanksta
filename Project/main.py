import pygame
import pygame_gui
import math
import os
from request import RequestServer
from offline import Offline


directory = str(os.path.abspath(os.getcwd())) + '/' # + '/Project/'


pygame.init()
pygame.display.set_caption("Tanksta")
screen = pygame.display.set_mode((1600, 900))
background = pygame.image.load(directory + 'assets/background2.png')
background = pygame.transform.scale(background, (1600, 900))

running = True
game_start = False
is_online = False

server = RequestServer()
manager = pygame_gui.UIManager((1600, 900))
clock = pygame.time.Clock()
online_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((750, 175), (100, 50)),
                                             text='Play Online',
                                             manager=manager)
offline_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((750, 100), (100, 50)),
                                             text='Play Offline',
                                             manager=manager)

while running:
    pygame.display.flip()
    time_delta = clock.tick(60)/1000.0
    screen.blit(background, (0, 0))
    
    if game_start:
        if is_online:
            server.checkGameIsFind()
        else:
            if not party.update(screen):
                game_start = False
    
    for event in pygame.event.get():
        if not game_start:
            manager.process_events(event)
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == online_button:
                        server.wantToPlay()
                        game_start = True
                        is_online = True
                    elif event.ui_element == offline_button:
                        game_start = True
                        is_online = False
                        party = Offline(2, 650, screen)
        if event.type == pygame.QUIT:
            pygame.quit()
            print("Game Closed")
            running = False

    if not game_start:
        manager.update(time_delta)
        manager.draw_ui(screen)
      
   
    