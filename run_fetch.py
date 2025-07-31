import os
import argparse
from dotenv import load_dotenv

from scripts.fetch_api import fetch_matches
from scripts.parse_matches import parse_matches
from scripts.save_to_csv import save_to_csv
from model.preprocess import add_simple_features, load_matches_from_csv, encode_teams, extract_date_features
from glob import glob
import pandas as pd

load_dotenv()
token = os.getenv("API_TOKEN")

def parse_args() -> list[dict]:
    parser = argparse.ArgumentParser(description="Fetch football matches for a given season.")
    parser.add_argument("--season", type=int, default=2023, help="Season year (e.g. 2023)")

    return {'season': parser.parse_args().season}

def fetch_and_save_raw_data(season: int):
    data = fetch_matches(token, season)
    parsed_data = parse_matches(data)
    save_to_csv(parsed_data, f"matches_{season}.csv")
    print(f"Fetched and saved {len(parsed_data)} games from {season}.")

def preprocess_all_static_data():
    csv_paths = glob("data/static/*.csv")

    dfs = []
    for path in csv_paths:
        df = load_matches_from_csv(path)
        df = encode_teams(df)
        df = extract_date_features(df)
        df = add_simple_features(df)
        dfs.append(df)

    full_df = pd.concat(dfs, ignore_index=True)
    print(full_df.head())

    full_df.to_csv("all_processed.csv", index=False)
    print(f"Saved {len(full_df)} matches to all_processed.csv")


def main():
    season = parse_args()['season']
    fetch_and_save_raw_data(season)
    preprocess_all_static_data()

if __name__ == "__main__":
    main()