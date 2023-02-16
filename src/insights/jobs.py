from functools import lru_cache
from typing import List, Dict


import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf8") as file:
        file_reader = csv.DictReader(file, delimiter=",", quotechar='"')
        file_list = []
        for item in file_reader:
            file_list.append(item)

        return file_list


def get_unique_job_types(path: str) -> List[str]:
    job_list = read(path)
    list_unique_job_types = []
    for job in job_list:
        if job["job_type"] not in list_unique_job_types:
            list_unique_job_types.append(job["job_type"])
    return list_unique_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    list_of_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            list_of_job_type.append(job)
    return list_of_job_type
