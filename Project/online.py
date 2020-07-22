import sys
import pygame

sys.path.append('controllers')
from controllers.player import Player
from tank import Tank

MOVEMENT_LIMIT = 120


class Online():
    numberOfPlayers = 0

    def __init__(self, server):
        if len(server.players) == 0:
            print("need more than 1 player")
            pygame.quit()
        print(server.players)
        self.server = server
        self.tanks = self.initTankPositions(server.players)
        self.player_tank = Tank(tuple([server.player['pos_x'], server.player['pos_y']]))
        self.player_tank.canon_angle = server.player['canon_orientation']
        self.tanks.append(self.player_tank)
        self.player = Player(self.player_tank)
        self.origin_position = None
        self.nextTurn = False

    def initTankPositions(self, players):
        tanks = []
        for player in players:
            print(tuple([player['pos_x'], player['pos_y']]))
            tanks.append(Tank(tuple([player['pos_x'], player['pos_y']])))
            tanks[len(tanks) - 1].canon_angle = player['canon_orientation']
        return tanks

    def update(self, screen):
        if self.server.current_player == None:
            print("error")

        if self.server.current_player['id'] == self.server.player['id']:
            if self.player.tank.current_health == 0 or self.nextTurn:
                self.origin_position = None
                self.server.endTurn()
                self.nextTurn = False
            else:
                if self.origin_position == None:
                    self.origin_position = [self.player.tank.body_rect.x, self.player.tank.body_rect.y]

                self.server.sendInfo(self.player.tank)
                for event in pygame.event.get():
                    self.player.controller(event)
                    if event.type == pygame.QUIT:
                        self.server.delete()
                        pygame.quit()
                        print("Game Closed")

                if self.difference_position(self.origin_position, self.player.tank.body_rect) > MOVEMENT_LIMIT or len(self.player.tank.bullets) >= 1:
                    self.nextTurn = True
        else:
            self.server.getInfo()
           

        for tank in self.tanks:
            tank.display(screen, self.tanks)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.server.delete()
                pygame.quit()
                print("Game Closed")

        return True

    def difference_position(self, pos1, pos2):
        return abs(pos1[0] - pos2.x) + abs(pos1[1] - pos2.y)