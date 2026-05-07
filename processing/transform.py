def transform_jobs(df):
    df["average_salary"] = (
        df["salary_from"] + df["salary_to"]
    ) / 2

    return df