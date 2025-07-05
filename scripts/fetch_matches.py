import requests
from datetime import datetime

response = requests.get("https://api.football-data.org/v4/competitions/PL/matches?season=2023", headers={"X-Auth-Token": "TOKEN"}, verify=False)

response_status_code = response.status_code
print(f"Status code: {response_status_code}")

data = response.json()
home_team = data['matches'][0]['homeTeam']['shortName']
away_team = data['matches'][0]['awayTeam']['shortName']

date = data['matches'][0]['utcDate']
datetime_object = datetime.fromisoformat(date[:-1])
formatted_date = datetime_object.strftime("%Y-%m-%d %H:%M:%S")

score_home = data['matches'][0]['score']['fullTime']['home']
score_away = data['matches'][0]['score']['fullTime']['away']

first_game = f"{home_team} {score_home} - {score_away} {away_team}, {formatted_date}"

print(first_game)
