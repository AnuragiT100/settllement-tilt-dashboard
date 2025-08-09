import pandas as pd
from prophet import Prophet
import pickle
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "settlement_log.csv"
MODEL_DIR = Path(__file__).resolve().parent.parent / "models"
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH, parse_dates=['timestamp'])
df_prophet = df.rename(columns={"timestamp": "ds", "settlement_mm": "y"})

# Remove timezone info from 'ds' column
df_prophet['ds'] = df_prophet['ds'].dt.tz_localize(None)

model = Prophet()
model.fit(df_prophet)

with open(MODEL_DIR / "prophet_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Prophet model trained and saved.")
