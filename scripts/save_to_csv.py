import pandas as pd

def save_to_csv(rows: list[dict], filename: str):
    df = pd.DataFrame(rows)
    df.to_csv(filename, index=False)