class Player:
    team_run = 0        #  Static variable        
    def __init__(self, run):
        self.run = run

    def hit_four(self):
        self.run += 4
        Player.team_run += 4
    
    def hit_six(self):
        self.run += 6
        Player.team_run += 6


sakib = Player(0)
Tazim = Player(0)

sakib.hit_four()
print(sakib.run)

Tazim.hit_six()
Tazim.hit_six()
print(Tazim.run)

print(f"Team run {Player.team_run}") # Team run 

