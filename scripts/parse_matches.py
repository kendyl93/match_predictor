from datetime import datetime

def parse_matches(data: dict) -> list[dict]:
    matches = data['matches']
    rows = []

    for match in matches:
        if match['status'] != 'FINISHED':
            continue

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

    return rows
