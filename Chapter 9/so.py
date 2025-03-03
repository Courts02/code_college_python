class StackOverflowed:
    def __init__(self, team_name="Stack Overflowed", team_size=5):
        self.team_name = team_name  
        self.team_size = team_size
        self.team_members = ["Ulrich", "Tom", "Courtney", "Lindo", "Phomello"]

    def describe_team(self):
        print(f"\n{self.team_name} has {self.team_size} members.")
        print(f"Team members: {self.team_members}")

team = StackOverflowed()
team.describe_team()
team.team_members.append("John")
team.describe_team()    