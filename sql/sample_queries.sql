-- Insert sample drivers
INSERT OR IGNORE INTO drivers (driver_id, name, churned) VALUES (1, 'Alice', 0);
INSERT OR IGNORE INTO drivers (driver_id, name, churned) VALUES (2, 'Bob', 1);
INSERT OR IGNORE INTO drivers (driver_id, name, churned) VALUES (3, 'Charlie', 0);

-- Insert sample experiments
INSERT OR IGNORE INTO experiments (experiment_id, name, description) VALUES (1, 'Flat Bonus vs Surge', 'Compare flat bonus payout to surge-based earnings');
INSERT OR IGNORE INTO experiments (experiment_id, name, description) VALUES (2, 'New Earnings Algorithm', 'Test new driver earnings algorithm');

-- Assign drivers to groups
INSERT OR IGNORE INTO assignments (driver_id, experiment_id, group_name) VALUES (1, 1, 'control');
INSERT OR IGNORE INTO assignments (driver_id, experiment_id, group_name) VALUES (2, 1, 'treatment');
INSERT OR IGNORE INTO assignments (driver_id, experiment_id, group_name) VALUES (3, 2, 'control');

-- Insert sample payouts
INSERT OR IGNORE INTO payouts (driver_id, earnings, payout_date) VALUES (1, 100.0, '2025-07-01');
INSERT OR IGNORE INTO payouts (driver_id, earnings, payout_date) VALUES (2, 120.0, '2025-07-01');
INSERT OR IGNORE INTO payouts (driver_id, earnings, payout_date) VALUES (3, 90.0, '2025-07-01');

-- Sample select: list all assignments for experiment 1
SELECT a.assignment_id, d.name AS driver_name, a.group_name
FROM assignments a
JOIN drivers d ON a.driver_id = d.driver_id
WHERE a.experiment_id = 1;

-- Sample select: average earnings by group for experiment 1
SELECT a.group_name, AVG(p.earnings) AS avg_earnings
FROM assignments a
JOIN payouts p ON a.driver_id = p.driver_id
WHERE a.experiment_id = 1
GROUP BY a.group_name;

-- Sample select: churn rate by group for experiment 1
SELECT a.group_name, AVG(d.churned) AS churn_rate
FROM assignments a
JOIN drivers d ON a.driver_id = d.driver_id
WHERE a.experiment_id = 1
GROUP BY a.group_name;
