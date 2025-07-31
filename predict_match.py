import argparse
import pandas as pd
from joblib import load

def parse_args():
    parser = argparse.ArgumentParser(description="Predicts match outcomes.")
    parser.add_argument("--home_team", type=str, required=True)
    parser.add_argument("--away_team", type=str, required=True)
    parser.add_argument("--weekday", type=int, required=True)
    parser.add_argument("--month", type=int, required=True)
    return parser.parse_args()

def main():
    args = parse_args()

    home_encoder = load("model/home_team_encoder.joblib")
    away_encoder = load("model/away_team_encoder.joblib")

    home_team_id = home_encoder.transform([args.home_team])[0]
    away_team_id = away_encoder.transform([args.away_team])[0]

    input_data = pd.DataFrame([{
        "home_team": home_team_id,
        "away_team": away_team_id,
        "weekday": args.weekday,
        "month": args.month,
        "is_weekend": int(args.weekday in [5, 6])
    }])

    model = load("model/model.joblib")
    probability = model.predict_proba(input_data)[0]

    print("Probabilities:")
    print(f"🤝 Draw:        {probability[0]:.2%}")
    print(f"🏠 Home win:   {probability[1]:.2%}")
    print(f"🚗 Away win:       {probability[2]:.2%}")

    

if __name__ == "__main__":
    main()
