### Activate venv

- activate `source venv/bin/activate`
- deactivate `deactivate`

### Install Packages

- `pip install -r requirements.txt`

### Fetching past games data

- `python3 run_fetch.py --season <year>`

### Training the model

- `python model/train_model.py`

### Running prediction

- `python predict_match.py --home_team "Arsenal" --away_team "Wolverhampton" --date 2025-09-09T23:00`

Result should be something like:
```
Probabilities:
🤝 Draw:        25.18%
🏠 Home win:   33.19%
🚗 Away win:       41.64%
```

### Adding deps to `requirements.txt`

- `pip freeze > requirements.txt`
