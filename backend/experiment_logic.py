import hashlib
from backend.database import get_db

def assign_driver_to_group(driver_id: int, experiment_id: int):
    # Hash driver+experiment to assign group deterministically
    hash_val = int(hashlib.sha256(f"{driver_id}-{experiment_id}".encode()).hexdigest(), 16)
    group = 'control' if hash_val % 2 == 0 else 'treatment'

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO assignments(driver_id, experiment_id, group_name)
        VALUES (?, ?, ?)
    """, (driver_id, experiment_id, group))
    conn.commit()
    conn.close()

    return group
