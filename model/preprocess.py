import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_matches_from_csv(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)

def encode_teams(df: pd.DataFrame) -> pd.DataFrame:
    le = LabelEncoder()
    df['home_team'] = le.fit_transform(df['home_team'])
    df['away_team'] = le.fit_transform(df['away_team'])
    return df

def extract_date_features(df: pd.DataFrame) -> pd.DataFrame:
    df['date'] = pd.to_datetime(df['date'])
    df['weekday'] = df['date'].dt.weekday
    df['month'] = df['date'].dt.month
    return df.drop(columns=['date'])

def add_simple_features(df: pd.DataFrame) -> pd.DataFrame:
    df['goal_diff'] = df['score_home'] - df['score_away']
    df['is_weekend'] = df['weekday'].isin([5, 6]).astype(int)
    return df
