import requests

def fetch_matches(token: str, season: int = 2023) -> dict:
    url = f"https://api.football-data.org/v4/competitions/PL/matches?season={season}"
    headers = {"X-Auth-Token": token}
    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching matches: {response.status_code}")
        return {"matches": []}
