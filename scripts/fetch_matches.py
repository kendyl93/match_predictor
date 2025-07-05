import requests
from datetime import datetime
import pandas as pd

response = requests.get("https://api.football-data.org/v4/competitions/PL/matches?season=2023", headers={"X-Auth-Token": "8a4ff920240a428a8d331524776e63be"}, verify=False)

response_status_code = response.status_code
print(f"Status code: {response_status_code}")

data = response.json()

matches = data['matches']

rows = []

for match in matches:
    home_team = match['homeTeam']['shortName']
    away_team = match['awayTeam']['shortName']
    date = match['utcDate']
    datetime_object = datetime.fromisoformat(date[:-1])
    formatted_date = datetime_object.strftime("%Y-%m-%d %H:%M:%S")
    score_home = match['score']['fullTime']['home']
    score_away = match['score']['fullTime']['away']

    if match['score']['winner'] == 'DRAW':
        winner = 0
    elif match['score']['winner'] == 'HOME_TEAM':
        winner = 1
    else:
        winner = 2

    row = {
        "home_team": home_team,
        "away_team": away_team,
        "date": formatted_date,
        "score_home": score_home,
        "score_away": score_away,
        "winner": winner
    }
    rows.append(row)

print(rows[2])

df = pd.DataFrame(rows)
df.to_csv("matches.csv", index=False)