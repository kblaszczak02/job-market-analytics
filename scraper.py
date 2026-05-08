import requests
import json
import time
import csv

URL = "https://justjoin.it/api/candidate-api/offers"

ITEMS_PER_PAGE = 100
MAX_CURSOR = 9900


def fetch_jobs(cursor=0):
    params = {
        "from": cursor,
        "itemsCount": ITEMS_PER_PAGE,
        "cityRadius": 30,
        "currency": "pln",
        "orderBy": "descending",
        "sortBy": "publishedAt",
        "keywordType": "any",
        "isPromoted": True
    }

    try:
        r = requests.get(URL, params=params, timeout=30)

        if r.status_code != 200:
            print(f"ERROR {r.status_code} dla cursor={cursor}")
            return None

        data = r.json()

        return data.get("data", [])

    except Exception as e:
        print(f"EXCEPTION dla cursor={cursor}: {e}")
        return None


def extract_salary(employment_types):
    if not employment_types:
        return None

    # preferuj PLN z widełkami
    for e in employment_types:
        if (
            e.get("currency") == "PLN"
            and e.get("from") is not None
        ):
            return e

    return employment_types[0]


def parse_job(job):
    salary = extract_salary(job.get("employmentTypes", []))

    required_skills = job.get("requiredSkills", [])
    nice_to_have = job.get("niceToHaveSkills", [])
    languages = job.get("languages", [])
    category = job.get("category", {})

    return {
        "id": job.get("guid"),
        "slug": job.get("slug"),
        "url": "https://justjoin.it/offers/" + job.get("slug", ""),

        "title": job.get("title"),
        "company": job.get("companyName"),
        "experience_level": job.get("experienceLevel"),
        "working_time": job.get("workingTime"),
        "workplace_type": job.get("workplaceType"),

        "city": job.get("city"),
        "street": job.get("street"),
        "latitude": job.get("latitude"),
        "longitude": job.get("longitude"),

        "category": category.get("key"),
        "parent_category": category.get("parentKey"),

        "salary_min": salary.get("from") if salary else None,
        "salary_max": salary.get("to") if salary else None,

        "salary_avg": (
            (salary.get("from") + salary.get("to")) / 2
            if salary
            and salary.get("from") is not None
            and salary.get("to") is not None
            else None
        ),

        "salary_currency": salary.get("currency") if salary else None,
        "salary_unit": salary.get("unit") if salary else None,
        "employment_type": salary.get("type") if salary else None,
        "gross": salary.get("gross") if salary else None,

        "required_skills": ", ".join(
            [s["name"] for s in required_skills]
        ) if required_skills else None,

        "nice_to_have_skills": ", ".join(
            [s["name"] for s in nice_to_have]
        ) if nice_to_have else None,

        "languages": ", ".join(
            [f'{l["code"]}:{l["level"]}' for l in languages]
        ) if languages else None,

        "published_at": job.get("publishedAt"),
        "expired_at": job.get("expiredAt"),
        "remote_interview": job.get("isRemoteInterview"),
        "open_to_ukrainians": job.get("isOpenToHireUkrainians"),
        "is_promoted": job.get("isPromoted"),
        "is_super_offer": job.get("isSuperOffer"),
        "apply_method": job.get("applyMethod"),
    }


def save_json(data, filename="jobs.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_csv(data, filename="jobs.csv"):

    if not data:
        return

    keys = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=keys)

        writer.writeheader()
        writer.writerows(data)


def main():
    all_jobs = []
    seen_ids = set()

    cursor = 0

    while cursor <= MAX_CURSOR:

        print(f"\nPobieranie cursor={cursor}")

        jobs = fetch_jobs(cursor)

        # retry gdy API padnie
        if jobs is None:
            print("Błąd API — retry za 5 sekund...")
            time.sleep(5)
            continue

        # koniec danych
        if not jobs:
            print("Brak kolejnych ofert.")
            break

        print(f"Pobrano: {len(jobs)}")

        added = 0

        for job in jobs:

            if not isinstance(job, dict):
                continue

            parsed = parse_job(job)

            # deduplikacja
            if parsed["id"] not in seen_ids:
                seen_ids.add(parsed["id"])
                all_jobs.append(parsed)
                added += 1

        print(f"Dodano nowych: {added}")
        print(f"Łącznie: {len(all_jobs)}")

        # checkpoint save
        save_json(all_jobs)
        save_csv(all_jobs)

        # kolejna strona
        cursor += ITEMS_PER_PAGE

        # throttle
        time.sleep(0.5)

    # final save
    save_json(all_jobs)
    save_csv(all_jobs)

    print("\nDONE")
    print(f"Finalnie zapisano {len(all_jobs)} ofert")


if __name__ == "__main__":
    main()