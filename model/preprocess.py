import pandas as pd
from sklearn.preprocessing import LabelEncoder
from joblib import dump

def load_matches_from_csv(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)

def encode_teams(df: pd.DataFrame) -> pd.DataFrame:
    home_encoder = LabelEncoder()
    away_encoder = LabelEncoder()

    df['home_team'] = home_encoder.fit_transform(df['home_team'])
    df['away_team'] = away_encoder.fit_transform(df['away_team'])

    dump(home_encoder, "model/home_team_encoder.joblib")
    dump(away_encoder, "model/away_team_encoder.joblib")

    return df

def extract_date_features(df: pd.DataFrame) -> pd.DataFrame:
    df['date'] = pd.to_datetime(df['date'])
    df['weekday'] = df['date'].dt.weekday
    df['month'] = df['date'].dt.month
    return df.drop(columns=['date'])

def add_simple_features(df: pd.DataFrame) -> pd.DataFrame:
    df['is_weekend'] = df['weekday'].isin([5, 6]).astype(int)
    return df
