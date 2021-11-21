class Player:
    def __init__(self, name, nationality, goals, assists):
        self.name = name
        self.nationality = nationality
        self.goals = goals
        self.assists = assists

    def __str__(self):
        return self.name + " from " + self.nationality + " goals: " + str(self.goals) + " assists: " + str(self.assists)
