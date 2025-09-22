import requests

teams_url = "https://sports.core.api.espn.com/v2/sports/football/leagues/nfl/seasons/2025/teams"
root = requests.get(teams_url).json()

scoreboard_url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
scoreboard_root = requests.get(scoreboard_url).json()

team_names = []
game_names = []

for item in root["items"]:
    ref_url = item["$ref"]               # the link to the team detail
    team_data = requests.get(ref_url).json()
    team_names.append(team_data["displayName"])  # or team_data["abbreviation"], etc.

for game in scoreboard_root["events"]:
    game_names.append(game["name"])



print(team_names)

print(game_names)
