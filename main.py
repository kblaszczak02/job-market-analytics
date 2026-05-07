from scraper.justjoinit_scraper import fetch_jobs
from processing.clean_data import clean_jobs
from processing.validate import validate_jobs
from processing.transform import transform_jobs
from processing.skill_parser import create_skills_table
from database.db import save_jobs
from config.settings import EXPORT_JOBS_PATH
from config.settings import EXPORT_SKILLS_PATH


print("Downloading jobs...")

jobs = fetch_jobs()

print("Cleaning data...")

cleaned = clean_jobs(jobs)

print("Validating data...")

validated = validate_jobs(cleaned)

print("Transforming data...")

transformed = transform_jobs(validated)

print("Creating skills table...")

skills_df = create_skills_table(transformed)

print("Saving database...")

save_jobs(transformed)

print("Exporting CSV files...")

transformed.to_csv(EXPORT_JOBS_PATH, index=False)
skills_df.to_csv(EXPORT_SKILLS_PATH, index=False)

print("Pipeline completed successfully.")