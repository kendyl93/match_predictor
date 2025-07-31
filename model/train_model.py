import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from joblib import dump

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def select_features(df: pd.DataFrame):
    X = df[["home_team", "away_team", "weekday", "month", "goal_diff", "is_weekend"]] 
    y = df["winner"]
    return X, y

def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {acc:.2f}")
    return model

def save_model(model, path: str):
    dump(model, path)
    print(f"Model saved to {path}")

def main():
    df = load_data("matches_2024_processed.csv")
    X, y = select_features(df)
    model = train_and_evaluate(X, y)
    save_model(model, "model/model.joblib")

if __name__ == "__main__":
    main()
