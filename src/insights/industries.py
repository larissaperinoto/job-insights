from typing import List, Dict

import src.insights.jobs as jobs


def get_unique_industries(path: str) -> List[str]:
    file_list = jobs.read(path)
    list_unique_industry = []
    for job in file_list:
        if job["industry"] not in list_unique_industry:
            list_unique_industry.append(job["industry"])
    return list_unique_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
