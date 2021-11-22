import requests
from player import Player

def is_finnish(player):
    if player.nationality == "FIN":
        return True
    else:
        return False

def points(player):
    return player.goals + player.assists

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'], player_dict['nationality'], player_dict['goals'], player_dict['assists'] )

        players.append(player)

    print("Oliot:")
    players = list(filter(is_finnish, players))
    players.sort(key=points, reverse=True)

    for player in players:
        print(player)
        
if __name__ == "__main__":
    main()
