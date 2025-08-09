import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Output path for the CSV file
OUT = os.path.join(os.path.dirname(__file__), "..", "data", "settlement_log.csv")

def generate(days=60, site_id="site01", lat=27.68, lon=85.32):
    start = datetime.utcnow() - timedelta(days=days)
    rows = []
    total_settlement = 0.0
    for i in range(days * 24):  # hourly data points
        ts = start + timedelta(hours=i)
        # Simulate cumulative settlement increasing slowly each hour (mm)
        total_settlement += np.random.normal(0.01, 0.005)
        # Simulate small tilt variations (degrees)
        tilt_x = np.random.normal(0, 0.002)
        tilt_y = np.random.normal(0, 0.002)
        rows.append([
            ts.isoformat() + "Z",  # Timestamp in ISO format with UTC indicator
            site_id,
            lat,
            lon,
            round(total_settlement, 4),
            round(tilt_x, 4),
            round(tilt_y, 4),
        ])
    df = pd.DataFrame(rows, columns=[
        'timestamp',
        'sensor_id',
        'latitude',
        'longitude',
        'settlement_mm',
        'tilt_x_deg',
        'tilt_y_deg'
    ])
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    df.to_csv(OUT, index=False)
    print(f"Generated simulated data CSV at: {OUT}")

if __name__ == "__main__":
    generate()
