from typing import List, Dict

import src.insights.jobs as jobs


def get_unique_industries(path: str) -> List[str]:
    file_list = jobs.read(path)
    list_unique_industries = []
    for job in file_list:
        if job["industry"] not in list_unique_industries and job["industry"]:
            list_unique_industries.append(job["industry"])
    return list_unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    list_jobs_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            list_jobs_by_industry.append(job)
    return list_jobs_by_industry
