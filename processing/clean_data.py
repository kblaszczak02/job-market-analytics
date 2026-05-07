import pandas as pd


def clean_jobs(jobs):
    df = pd.DataFrame(jobs)

    df = df.drop_duplicates()

    df["city"] = df["city"].fillna("Unknown")

    df["salary_from"] = df["salary_from"].fillna(0)
    df["salary_to"] = df["salary_to"].fillna(0)

    return df