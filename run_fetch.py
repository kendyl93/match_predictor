import os
import argparse
from dotenv import load_dotenv

from scripts.fetch_api import fetch_matches
from scripts.parse_matches import parse_matches
from scripts.save_to_csv import save_to_csv
from model.preprocess import add_simple_features, load_matches_from_csv, encode_teams, extract_date_features

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

    df = load_matches_from_csv(f"data/static/matches_{season}.csv")
    df = encode_teams(df)
    df = extract_date_features(df)
    df = add_simple_features(df)
    print(df)
    df.to_csv(f"matches_{season}_processed.csv", index=False)

if __name__ == "__main__":
    main()