import requests
import json

class RequestServer():
    def __init__(self):
        self.player = None

    def wantToPlay(self):
        payload = {'pseudo': 'losabit'}
        r = requests.post('http://127.0.0.1:8000/players/', data=payload)
        self.player = json.loads(r.text)

    def checkGameIsFind(self):
        if self.player == None:
            return
        r = requests.get("http://127.0.0.1:8000/players/" + str(self.player["id"]) + "/?format=json")
        result = json.loads(r.text)
        if result["play_on"] is not None:
            self.loadGame(result["play_on"])

    def loadGame(self, id):
        print("t")

    def deleteAll(self):
        print("t")