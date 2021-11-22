from player import Player
import requests

class PlayerReader:
    def __init__(self, url):
        self.url = url
        response = requests.get(self.url).json()

        #print("JSON-muotoinen vastaus:")
        #print(response)

        self.players = []

        for player_dict in response:
            player = Player(
                player_dict['name'], player_dict['nationality'], player_dict['goals'], player_dict['assists'] )

            self.players.append(player)