class PlayerStats:
    def __init__(self, reader):
        self.players = reader.players
    
    def top_scorers_by_nationality(self, nationality):
        self.nationality = nationality
        self.players = list(filter(self.right_nationality, self.players))
        self.players.sort(key=self.points, reverse=True)
        return self.players
    def right_nationality(self, player):
        if player.nationality == self.nationality:
            return True
        else:
            return False

    def points(self, player):
        return player.goals + player.assists