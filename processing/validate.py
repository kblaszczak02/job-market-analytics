def validate_jobs(df):
    df = df[df["title"].notnull()]

    df = df[df["salary_from"] <= df["salary_to"]]

    return df