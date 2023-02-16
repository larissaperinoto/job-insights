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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
