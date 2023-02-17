from typing import Union, List, Dict


import src.insights.jobs as jobs


def get_max_salary(path: str) -> int:
    file_list = jobs.read(path)
    list_max_salaries = []
    for job in file_list:
        if job["max_salary"] and job["max_salary"] != 'invalid':
            list_max_salaries.append(int(job["max_salary"]))
    return max(list_max_salaries)


def get_min_salary(path: str) -> int:
    file_list = jobs.read(path)
    list_min_salaries = []
    for job in file_list:
        if job["min_salary"] and job["min_salary"] != 'invalid':
            list_min_salaries.append(int(job["min_salary"]))
    return min(list_min_salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        if int(job['min_salary']) <= int(salary) <= int(job['max_salary']):
            return True
        else:
            return False
    except (TypeError, KeyError):
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
