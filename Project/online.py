import sys
import pygame
import pygame_gui
sys.path.append('controllers')
from controllers.player import Player
from tank import Tank
from gui import GUI

MOVEMENT_LIMIT = 120


class Online():
    numberOfPlayers = 0

    def __init__(self, server):
        if len(server.players) == 0:
            print("need more than 1 player")
            pygame.quit()
        print(server.players)
        self.server = server
        self.ids = self.initIds(server.players)
        self.tanks = self.initTankPositions(server.players)
        self.player_tank = Tank(tuple([server.player['pos_x'], server.player['pos_y']]))
        self.player_tank.moveCanon(server.player['canon_orientation'] - self.player_tank.canon_angle)
        self.tanks.append(self.player_tank)
        self.player = Player(self.player_tank)
        self.origin_position = None
        self.nextTurn = False
        self.last_indice = -1
        self.last_player = None
        self.manager = pygame_gui.UIManager((1600, 900))
        self.gui = GUI(self.tanks, manager=self.manager)

    def initTankPositions(self, players):
        tanks = []
        for player in players:
            tanks.append(Tank(tuple([player['pos_x'], player['pos_y']])))
            tanks[len(tanks) - 1].moveCanon(player["canon_orientation"] - tanks[len(tanks) - 1].canon_angle)
        return tanks

    def initIds(self, players):
        ids = {}
        count = 0
        for player in players:
            ids[player['id']] = count
            count += 1
        return ids

    def update(self, screen):

        self.gui.draw(0, screen)
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
                    self.player.update()
                    if event.type == pygame.QUIT:
                        self.server.delete()
                        pygame.quit()
                        print("Game Closed")

                if self.difference_position(self.origin_position, self.player.tank.body_rect) > MOVEMENT_LIMIT or len(self.player.tank.bullets) >= 1:
                    self.nextTurn = True
        else:
            self.server.getInfo()
            current_player = self.server.current_player
            if current_player["id"] in self.ids:
                indice = self.ids[current_player["id"]]
                self.tanks[indice].move(current_player["pos_x"] - self.tanks[indice].body_rect.x)
                self.tanks[indice].current_health = current_player["health"]
                self.tanks[indice].moveCanon(current_player["canon_orientation"] - self.tanks[indice].canon_angle)
                if self.last_indice == -1:
                    self.last_indice = indice
                    self.last_player = current_player
                if self.last_indice != indice: 
                    self.tanks[indice].shoot(self.last_player["puissance"])
                    self.last_indice = indice
                    self.last_player = current_player

        for tank in self.tanks:
            if tank.current_health != 0:
                tank.display(screen, self.tanks)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.server.delete()
                pygame.quit()
                print("Game Closed")

        return True

    def difference_position(self, pos1, pos2):
        return abs(pos1[0] - pos2.x) + abs(pos1[1] - pos2.y)