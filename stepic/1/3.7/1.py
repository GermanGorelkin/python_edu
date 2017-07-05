class Team:
    def __init__(self, name, victory=0, draw=0, defeat=0):
        self.name = name
        self.victory = victory
        self.draw = draw
        self.defeat = defeat

    def __str__(self):
        return '{0}:{1} {2} {3} {4} {5}'.format(
            self.name, self.get_number_of_games(),
            self.victory, self.draw, self.defeat, self.get_points())

    def get_number_of_games(self):
        return self.victory + self.draw + self.defeat

    def get_points(self):
        return self.victory * 3 + self.draw


n = int(input())
result = dict()
for i in range(n):
    s = input()
    l = s.split(';')
    team1_name = l[0]
    team1_score = l[1]
    team2_name = l[2]
    team2_score = l[3]

    team1 = result.get(team1_name, Team(team1_name))
    team2 = result.get(team2_name, Team(team2_name))

    if team1_score == team2_score:
        team1.draw += 1
        team2.draw += 1
    elif team1_score > team2_score:
        team1.victory += 1
        team2.defeat += 1
    else:
        team1.defeat += 1
        team2.victory += 1

    result[team1_name] = team1
    result[team2_name] = team2

for v in result.values():
    print(v)
