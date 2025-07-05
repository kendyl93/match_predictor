from scripts.fetch_api import fetch_matches
from scripts.parse_matches import parse_matches
from scripts.save_to_csv import save_to_csv

def main():
    token = ''
    data = fetch_matches(token)
    parsed_data = parse_matches(data)
    save_to_csv(parsed_data, "matches.csv")

if __name__ == "__main__":
    main()