import pandas as pd
import random
import sqlite3

DB_PATH = "./data/experiment.db"
random.seed(42)

# Generate sample drivers
drivers = pd.DataFrame({
    'driver_id': list(range(1, 101)),
    'signup_time': pd.date_range("2022-01-01", periods=100, freq='D'),
    'churned': [random.randint(0, 1) for _ in range(100)]
})

# Generate payouts
payouts = pd.DataFrame({
    'driver_id': drivers['driver_id'],
    'earnings': [round(random.uniform(100, 300), 2) for _ in range(100)],
    'date': pd.date_range("2022-03-01", periods=100, freq='D')
})

conn = sqlite3.connect(DB_PATH)
drivers.to_sql("drivers", conn, if_exists="replace", index=False)
payouts.to_sql("payouts", conn, if_exists="replace", index=False)
conn.close()
