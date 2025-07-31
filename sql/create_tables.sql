-- Drivers table
CREATE TABLE IF NOT EXISTS drivers (
    driver_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    churned BOOLEAN DEFAULT 0
);

-- Experiments table
CREATE TABLE IF NOT EXISTS experiments (
    experiment_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
);

-- Assignments table
CREATE TABLE IF NOT EXISTS assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_id INTEGER NOT NULL,
    experiment_id INTEGER NOT NULL,
    group_name TEXT NOT NULL,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(driver_id, experiment_id),
    FOREIGN KEY(driver_id) REFERENCES drivers(driver_id),
    FOREIGN KEY(experiment_id) REFERENCES experiments(experiment_id)
);

-- Payouts table
CREATE TABLE IF NOT EXISTS payouts (
    payout_id INTEGER PRIMARY KEY AUTOINCREMENT,
    driver_id INTEGER NOT NULL,
    earnings REAL NOT NULL,
    payout_date DATE NOT NULL,
    FOREIGN KEY(driver_id) REFERENCES drivers(driver_id)
);
