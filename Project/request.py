import requests
import json
#https://fr.python-requests.org/en/latest/user/quickstart.html
url = 'http://127.0.0.1:8000'
class RequestServer():
    def __init__(self):
        self.player = None

    def wantToPlay(self):
        payload = {'pseudo': 'losabit'}
        r = requests.post(url + '/players/', data=payload)
        self.player = json.loads(r.text)

    def checkGameIsFind(self):
        if self.player is None:
            return
        r = requests.get(url + "/players/" + str(self.player["id"]) + "/?format=json")
        result = json.loads(r.text)
        if result["play_on"] is not None:
            self.loadGame(result["play_on"])

    def loadGame(self, game_id, tank):
        self.player["health"] = tank.health
        self.player["pos_x"] = tank.body_rect.x
        self.player["pos_y"] = tank.body_rect.y
        self.player["canon_orientation"] = tank.canon_angle
        r = requests.put(url + '/players/' + str(self.player["id"]), data=self.player)
        count = 0
        r = requests.get(url+'/players/'+"/?format=json")
        for p in result:
            if p["play_on"] == self.player["play_on"]:
                count +=1
        return result["play_on"]

    def deleteAll(self):
        print("t")

