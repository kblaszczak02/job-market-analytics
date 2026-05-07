from scraper.api_client import fetch_jobs_from_api


def fetch_jobs():
    raw_jobs = fetch_jobs_from_api()

    jobs = []

    for job in raw_jobs:
        job_data = {
            "title": job.get("title"),
            "company": job.get("company_name"),
            "city": job.get("city"),
            "remote_type": job.get("workplace_type"),
            "salary_from": job.get("salary_from"),
            "salary_to": job.get("salary_to"),
            "experience": job.get("experience_level"),
            "skills": extract_skills(job),
        }

        jobs.append(job_data)

    return jobs


def extract_skills(job):
    skills = []

    required_skills = job.get("skills", [])

    for skill in required_skills:
        skills.append(skill.get("name"))

    return skills