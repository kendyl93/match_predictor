import os
import argparse
from dotenv import load_dotenv

from scripts.fetch_api import fetch_matches
from scripts.parse_matches import parse_matches
from scripts.save_to_csv import save_to_csv

load_dotenv()
token = os.getenv("API_TOKEN")

def parse_args() -> list[dict]:
    parser = argparse.ArgumentParser(description="Fetch football matches for a given season.")
    parser.add_argument("--season", type=int, default=2023, help="Season year (e.g. 2023)")

    return {'season': parser.parse_args().season}


def main():
    season = parse_args()['season']
    data = fetch_matches(token, season)
    parsed_data = parse_matches(data)
    save_to_csv(parsed_data, f"matches_{season}.csv")
    print(f"Fetched and saved {len(parsed_data)} games from {season}.")

if __name__ == "__main__":
    main()