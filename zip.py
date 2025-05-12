# 🎯 Goal: Use zip() to pair football players with the teams they played for

# List of famous football players
players = ["Ronaldo", "Messi", "Hazard", "Aguero"]

# Their respective clubs (historical/famous association)
teams = ["Real Madrid", "Barcelona", "Chelsea", "Manchester City"]

# ⛓️ Pair players with teams using zip
paired_players_and_teams = zip(players, teams)
#The above represents a zip object

# Convert the zip object to a paired list (tuples)
player_team_list = list(paired_players_and_teams)

# Print each pairing in a readable format
print("\n📋 Who played for who?\n")
#\n is basically another way of pressing enter/skipping a line
for player, team in player_team_list:
    # Each item in the list is a pair (a tuple), so the loop unpacks both player and team in each round.
    print(f"⚽ {player} played for {team}")
