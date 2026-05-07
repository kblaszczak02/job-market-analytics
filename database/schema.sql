CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    city TEXT,
    remote_type TEXT,
    salary_from INTEGER,
    salary_to INTEGER,
    average_salary REAL,
    experience TEXT
);