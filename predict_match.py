import argparse
import pandas as pd
from joblib import load

def parse_args():
    parser = argparse.ArgumentParser(description="Predicts match outcomes.")
    parser.add_argument("--home_team", type=int, required=True)
    parser.add_argument("--away_team", type=int, required=True)
    parser.add_argument("--weekday", type=int, required=True)
    parser.add_argument("--month", type=int, required=True)
    return parser.parse_args()

def main():
    args = parse_args()

    input_data = pd.DataFrame([{
        "home_team": args.home_team,
        "away_team": args.away_team,
        "weekday": args.weekday,
        "month": args.month
    }])

    model = load("model/model.joblib")
    probability = model.predict_proba(input_data)[0]

    print("Probabilities:")
    print(f"🤝 Draw:        {probability[0]:.2%}")
    print(f"🏠 Home win:   {probability[1]:.2%}")
    print(f"🚗 Away win:       {probability[2]:.2%}")

    

if __name__ == "__main__":
    main()
# python predict_match.py --home_team 13 --away_team 8 --weekday 5 --month 8
