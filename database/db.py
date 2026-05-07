import sqlite3
from config.settings import DATABASE_PATH


def save_jobs(df):
    connection = sqlite3.connect(DATABASE_PATH)

    df.to_sql(
        "jobs",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()