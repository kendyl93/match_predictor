from dotenv import load_dotenv
import os

from scripts.fetch_api import fetch_matches
from scripts.parse_matches import parse_matches
from scripts.save_to_csv import save_to_csv

load_dotenv()
token = os.getenv("API_TOKEN")

season = 2024

def main():
    data = fetch_matches(token, season)
    parsed_data = parse_matches(data)
    save_to_csv(parsed_data, f"matches_{season}.csv")
    print(f"Fetched and saved {len(parsed_data)} games from {season}.")

if __name__ == "__main__":
    main()