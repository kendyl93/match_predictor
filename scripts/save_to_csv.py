import os
import pandas as pd

def save_to_csv(rows: list[dict], filename: str, path: str = 'data/static'):
    os.makedirs(path, exist_ok=True)
    df = pd.DataFrame(rows)
    df.to_csv(f"{path}/{filename}", index=False)