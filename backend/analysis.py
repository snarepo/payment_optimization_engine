import pandas as pd
from backend.database import get_db

def get_experiment_metrics(experiment_id: int):
    conn = get_db()
    query = """
        SELECT a.group_name, p.earnings, d.churned
        FROM assignments a
        JOIN payouts p ON a.driver_id = p.driver_id
        JOIN drivers d ON d.driver_id = a.driver_id
        WHERE a.experiment_id = ?
    """
    df = pd.read_sql_query(query, conn, params=(experiment_id,))
    result = df.groupby("group_name").agg({"earnings": "mean", "churned": "mean"}).reset_index()
    return result.to_dict(orient="records")
