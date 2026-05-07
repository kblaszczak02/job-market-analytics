import pandas as pd


def create_skills_table(df):
    rows = []

    for index, row in df.iterrows():
        skills = row["skills"]

        if isinstance(skills, list):
            for skill in skills:
                rows.append({
                    "job_title": row["title"],
                    "skill": skill
                })

    return pd.DataFrame(rows)